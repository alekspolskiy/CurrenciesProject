<template>
<!--  <Loader/>-->
  <div  class="row">
     <HomeCurrency/>
  </div>
</template>

<script>
import HomeCurrency from "@/components/app/HomeCurrency";
// import Loader from "@/components/app/Loader";
export default {
  name: "Home",
  data: () => ({
    loading: true,
  }),
  components: {
    // Loader,
    HomeCurrency
  },

}
</script>

<style scoped>

</style>