"""Module to setup fastapi API to expose API to the outside world."""
import logging
import random
from typing import Any, Dict
from starlette.datastructures import State
from ._utils import get_code_dict, get_intersection
from fastapi import FastAPI
import uvicorn
from .models import Resolved

ERROR_CODES = [error_code for error_code in range(50)]
LOGGER = logging.getLogger("API")
logging.basicConfig(filename='file.log', filemode='w', level=logging.INFO)

app = FastAPI()

app.state = {
    "error_count" : 0,
    "get_list" : {},
    }



def _generate_lists() -> Dict[str, Any]:
    """Generate resolved, unresolved and backlog lists."""
    return {
        'resolved': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error ABC occured, that is `resolved`'
        } for error_idx in range(50)],
        'unresolved': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error DEF occured, that is `unresolved`'
        } for error_idx in range(50, 100)],
        'backlog': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error XYZ occured, that is in the `backlog`'
        } for error_idx in range(100, 150)]
    }

@app.get("/get_lists")
def get_lists(operator_name  = "") -> Dict[str, Any]:
    """Return resolved, unresolved and backlog lists."""
    LOGGER.info('Generating resolved, unresolved and backlog lists.')
    app.state['error_count'] =  app.state.get('error_count') + 1
    app.state["get_list"][operator_name] = app.state["get_list"].get(operator_name, 0) + 1
    LOGGER.info(f"Accessed {app.state.get('error_count')} time(s) in total")
    LOGGER.info(f"Operator- {operator_name} accessed the list {app.state['get_list'].get(operator_name, 0)} time(s)")
    return _generate_lists()


@app.get("/get_list_intersection_counts")
def get_list_intersection_counts() -> Dict[str, int]:
    """Return the error intersection counts between a set of resolved, unresolved and backlog lists.

    Returns
    -------
    intersection_counts: Dict[str, int]
        The intersection counts between resolved, unresolved and backlog lists, e.g.:
        ```json
        {
            "resolved_unresolved": 12,
            "resolved_backlog": 6,
            "unresolved_backlog": 35
        }
        ```
        `"resolved_unresolved": 12` describes that there are `12` errors with the *same error code*  shared
        between a `resolved` and `unresolved` list, `"resolved_backlog": 6` describes that there are `6`
        errors with the *same error code*  shared between a `resolved` and `backlog` list.

        The three lists required for this calculation are generated by calling `_generate_lists`.

        Code that checks whether errors from the resolved and unresolved list `intersect`, could look like:
        ```python
        error_lists = _generate_lists()
        resolved, unresolved, backlog = error_lists['resolved'], error_lists['unresolved'], error_lists['backlog']

        error_from_resolved = resolved[0]
        error_from_unresolved  = unresolved[0]
        if error_from_resolved.code == error_from_unresolved.code:
            print('Errors intersect')
        else:
            print('Errors do not intersect')
        ```

    """
    LOGGER.info('Generating the intersection counts between a set of resolved, unresolved and backlog lists.')

    error_lists = _generate_lists()
    resolved, unresolved, backlog = error_lists['resolved'], error_lists['unresolved'], error_lists['backlog']
    
    resolved_dict = get_code_dict(resolved)
    unresolved_dict = get_code_dict(unresolved)
    backlog_dict = get_code_dict(backlog)
    
    resolve_unresolved = get_intersection(resolved_dict, unresolved_dict)
    resolved_backlog = get_intersection(resolved_dict, backlog_dict)
    unresolved_backlog = get_intersection(unresolved_dict, backlog_dict)
    


    # TODO: Implement the code that calculates how many errors with *the same error code* are shared between
    # the possible pairs of lists here. Then return a Dict like the one shown in the documentation string above,
    # e.g.:
    return  {
        'resolved_unresolved': resolve_unresolved,
        'resolved_backlog': resolved_backlog,
        'unresolved_backlog': unresolved_backlog
    }
    # NOTE: THIS IS JUST AN EXAMPLE, REPLACE WITH YOUR OWN CODE AND `return`!

@app.post("/post-resolved", status_code=200)
def post_resolved(resolved_list: list[Resolved]):
    resolved_errors = {}
    
    for error in resolved_list:
        resolved_errors[error.code] = resolved_errors.get(error.code, 0) + 1
    
    LOGGER.info(resolved_errors)
    
    return resolved_errors
    

def run(host: str, port: int) -> None:
    """Run the code challenge API."""
    uvicorn.run(app, host=host, port=port)
    
