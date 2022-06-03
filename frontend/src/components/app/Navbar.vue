<template>
    <nav class="navbar orange lighten-1">
      <div class="nav-wrapper">
        <div class="navbar-left">
          <a href="#" @click.prevent="$emit('click')">
          </a>
        </div>

      </div>
    </nav>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>

</style>