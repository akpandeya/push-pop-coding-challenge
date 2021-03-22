<template>
    <div class="table__div">
        <table class="custom__table" v-show="data.length > 0">
            <thead>
                <tr>
                    <th v-for="column in columns" :key="column">
                        <span class = "text">
                            {{column}}
                        </span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in data" :key="row.index">
                    <td  scope="row"   v-for="(col, i) in columnNames" :label='columns[i]' :key="col">{{row[col]}}</td> 
                    <td scope="row" ><button v-bind:class='[button.class]' v-on:click='() => {handleClick (row.index, button.class)}'> <span>{{button.label}}</span></button></td>
                </tr>
            </tbody>
        </table>
        <a v-show="data.length == 0">
            Table is empty!
        </a>        
    </div>
</template>

<script>

import {handleClick} from "./utils"

export default {
    props: ['columns', 'columnNames', 'data', 'button'],
    methods: {
        handleClick

    }
}
</script>
