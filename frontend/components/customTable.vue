<template>
    <div class="table__div">
        <table class="custom__table">
            <thead>
                <tr>
                    <th v-for="column in columns" :key="column">
                        {{column}}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in data" :key="row.index">
                    <td  scope="row"   v-for="(col, i) in columnNames" :label='columns[i]' :key="col">{{row[col]}}</td> 
                    <td scope="row" ><button v-bind:class='[button.class]' v-on:click='() => {handleClick (row.index, button.class)}'>{{button.label}}</button></td>
                </tr>
            </tbody>
        </table>
        <button class="undo__last tooltip" v-on:click='() => {handleClick (null, "undo-last")}'>
            <svg viewBox="0 0 423.642 423.642" >
                <path  d="M342.369,37.498h43.755v-30H272.128v113.995h30V46.501c78.268,44.711,113.054,141.985,77.673,227.401
                c-28.973,69.949-96.829,112.248-168.216,112.242c-23.142-0.002-46.667-4.45-69.343-13.842c-44.869-18.586-79.815-53.532-98.4-98.401
                c-18.585-44.869-18.585-94.29,0-139.159l-27.717-11.48c-44.696,107.907,6.729,232.059,114.636,276.756
                c26.424,10.945,53.818,16.126,80.784,16.125c83.158-0.001,162.221-49.278,195.972-130.762
                C444.692,195.637,415.368,94.662,342.369,37.498z"/>
            </svg>
            <span class="tooltiptext">Undo</span>
        </button>                         
    </div>
</template>

<script>

export default {
    props: ['columns', 'columnNames', 'data', 'button'],
    methods: {
        handleClick (index, type) {

            // console.log("Button Clicked", index, type)
            this.$emit('button-click', {
                index : index,
                type : type
            });
            
        },

    }
}
</script>
