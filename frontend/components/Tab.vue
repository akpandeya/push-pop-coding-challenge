<template lang="html">
  <div v-show='isActive'>

    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'Tab'
    },
    count: Number,
    icon : String,
  },
  data () {
    return {
      isActive: true
    }
  }
}
</script>