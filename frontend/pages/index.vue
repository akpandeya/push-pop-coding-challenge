<template>
  <div 
    :set="title= [`Resolved: ${resolved.length}`, `Unresolved: ${unresolved.length}`, `Backlog: ${backlog.length}`, `History: ${history.length}`]"
    >
    <tabs>
      <tab :title = title[0]>
        <custom-table
          v-bind:columns='errorTableColumns'
          v-bind:data='resolved'
          v-bind:button='{
            label: "Unresolve",
            class : "unresolve"
          }'
          v-bind:columnNames='errorColumnNames'
          action="Unresolve"
          buttonClass="resolve"
          @button-click="handleButtonClick"
        >
        </custom-table>
      </tab>
      <tab :title = title[1]>
        <custom-table
          v-bind:columns='errorTableColumns'
          v-bind:data='unresolved'
          v-bind:button='{
            label: "Resolve",
            class : "resolve"
          }'
          v-bind:columnNames='errorColumnNames'
          @button-click="handleButtonClick"
        >
        </custom-table>
      </tab>
      <tab :title = title[2]>
        <custom-table
          v-bind:columns='errorTableColumns'
          v-bind:data='backlog'
          v-bind:button='{
            label: "Move to Unresolved",
            class : "moveToUnresolved"
          }'
          v-bind:columnNames='errorColumnNames'
          @button-click="handleButtonClick"
        >
        </custom-table>
      </tab>
      <tab :title = title[3]>
        <custom-table
          v-bind:columns='["Code", "Text", "Action"]'
          v-bind:data='history'
          v-bind:button='{
            label: "Move Back",
            class : "undo"
          }'
          v-bind:columnNames='["code", "text", "action"]'
          @button-click="handleButtonClick"
        >
        </custom-table>
      </tab>
    </tabs>
  </div>
</template>

<script>
import Tab from '../components/Tab.vue';
import Tabs from '../components/Tabs';
import customTable from '../components/customTable.vue';
import {moveItemGetHistory, handleButtonClick, undoMove} from './utils'
export default {
  components: { customTable, Tabs, Tab },
  async asyncData({ $axios }) {
    try {
      const { resolved, unresolved, backlog } = await $axios.$get(
        "http://localhost:8000/get_lists",
        {
          params: {
            operator_name: 'akpandeya'
          }
        }
      );

      return {
        resolved,
        unresolved,
        backlog
      };
    } catch (error) {
      console.log(
        `Couldn't get error lists:\n${error}\nDid you start the API?`
      );
      console.log(
        "HINT: You can comment out the full `asyncData` method and work with mocked data for UI/UX development, if you want to."
      );
    }
  },
  data() {
    return {
      resolved: [],
      unresolved: [],
      backlog: [],
      history: [],
      errorTableColumns: ["Code", "Error", "Text"],
      errorColumnNames: ['code', 'text']
    };
  },
  methods: {
    handleButtonClick,

    moveItemGetHistory,

    undoMove,

    
  },


};
</script>
