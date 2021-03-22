<template lang="html">
  <div class="main-grid">
     <nav class="main-nav">
        <ul class="main-nav-list">
            <li class="main-nav-item"
            v-for='(tab, index) in tabs'
                :key='tab.title'
                @click='selectTab(index)'
                >
                <a class="menu-item" :class='{"is-selected": (index == selectedIndex)}'>

                  <span class="icon"> {{tab.icon}} </span>
                  <span class="text">{{ tab.title }}</span>
                  <span class="count">: {{ tab.count }}</span>
                </a> 
            </li>
            <button 
              class="undo-button" 
              :disabled='undoDisabled' 
              :class='undoDisabled' 
              v-on:click='() => {handleClick (null, "undo-last")}'
            >
              <a class="menu-item">
                <span class="text">Undo</span>
              </a>
            </button> 

            <button class="undo-all" v-on:click='() => {handleClick (null, "undo-all")}'>
              <a class="menu-item">
                <span class="text">Undo All</span>
              </a>
            </button> 
        </ul>
      </nav>
      
    <main class="main-content">
   
      <slot></slot>
    </main>

  </div>
</template>

<script>
import {handleClick} from './utils';
export default {

  props : {
    undoDisabled : Boolean,

  },
  
  data () {
    return {
      selectedIndex: 0, // the index of the selected tab,
      tabs: []         // all of the tabs
    }
  },
  created () {
    this.tabs = this.$children
  },
  mounted () {
    this.selectTab(0)
  },
  methods: {
    selectTab (i) {
      this.selectedIndex = i

      // loop over all the tabs
      this.tabs.forEach((tab, index) => {
        tab.isActive = (index === i)
      })
    },
    handleClick
    
  }
}
</script>