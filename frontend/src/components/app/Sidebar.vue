<template>
    <ul class="sidenav app-sidenav" :class="{open: true}">
      <li>
        <a href="/main" class="waves-effect waves-orange pointer">Currencies</a>
      </li>
    </ul>
</template>

<script>
export default {
  props: ['value']
}
</script>

<style scoped>

</style>