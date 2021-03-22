<template>
  <div>
    <tabs @button-click="handleButtonClick" :undoDisabled='this.history.length === 0'>
      <tab title = 'Resolved' :count='resolved.length' icon="R">
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
      <tab title = 'Unresolved' :count='unresolved.length' icon="U">
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
      <tab title = 'Backlog' :count='backlog.length' icon="B">
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
      <tab title = 'History' :count='history.length' icon="H">
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
import SnackBar from '../components/SnackBar'
import {moveItemGetHistory, handleButtonClick, undoMove, undoAll} from './utils'
export default {
  components: { customTable, Tabs, Tab, SnackBar },
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
      errorTableColumns: ["Code", "Text", ""],
      errorColumnNames: ['code', 'text']
    };
  },
  methods: {
    handleButtonClick,

    moveItemGetHistory,

    undoMove,

    undoAll,
  },


};
</script>
