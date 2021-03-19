export function moveItemGetHistory(index, source, target, text="", newPosition=-1,)
{

    const oldPosition = source.findIndex(item => item.index == index);
    console.log(oldPosition)
    if (oldPosition > -1) {

      const item = source[oldPosition];
      source.splice(oldPosition, 1);
      if (newPosition == -1){
        newPosition = target.length
      }
      target.splice(newPosition, 0, item);

    
    

    return ({
      code: item.code,
      text: item.text,
      oldPosition: oldPosition,
      newPosition: newPosition,
      source: source,
      target: target,
      index: index,
      action: `moved from ${text}`
    })
  }
    
}

export function handleButtonClick(value) 
{
  console.log('From the child:', value);

  switch (value.type){
    case 'resolve':
      this.history.push(this.moveItemGetHistory(value.index, this.$data.unresolved, this.$data.resolved, "unresolved to resolved"))
      break;
    case 'unresolve':
      this.history.push(this.moveItemGetHistory(value.index, this.$data.resolved, this.$data.unresolved, "resolved to unresolved"))
      break;
    case 'moveToUnresolved':
      this.history.push(this.moveItemGetHistory(value.index, this.$data.backlog, this.$data.unresolved, "backlog to unresolved"))
      break;
    case 'undo':
      this.undoMove(this.history.findIndex(item => item.index == value.index))
      break;
    case 'undo-last':
      this.undoMove(this.history.length - 1)
      break;
    default:
      console.log("Do not recognise this button. It should have class 'resolve', 'unresolve', 'moveToUnresolved', 'undo'");
  }
}

export function undoMove(position){
  if (position !== -1)
  {
    const move = this.history[position]
    if(move){
      moveItemGetHistory(move.index, move.target, move.source, move.old_position)
    }
    this.history.splice(position, 1);
  }
}