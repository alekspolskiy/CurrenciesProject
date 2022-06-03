<template>
    <v-dialog
        v-if="showPrice"
        v-model="showPrice"
        persistent
        max-width="60%"
    >
      <v-card
        class="mx-auto text-center"
        color="green"
        dark
      >
        <v-card-text>
          <v-sheet color="rgba(0, 0, 0, .12)">
            <v-sparkline
              :value="$store.getters.getPriceByCurrency(currency.currency_id)"
              color="rgba(255, 255, 255, .7)"
              height="100"
              padding="24"
              stroke-linecap="round"
              smooth
            >
              <template v-slot:label="item">
                {{ item.value }}
              </template>
            </v-sparkline>
          </v-sheet>
        </v-card-text>

        <v-card-text>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions class="justify-center">
          <v-divider></v-divider>
          <v-btn
                    color="red"
                    plain
                    @click="clearPrice()"
                >
                    Close
                </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

</template>

<script>


export default {
    name: "PriceModal",
    props: ['currency'],
    data(){
        return {
          value: [],
        }
    },
    computed: {
        showPrice: function() {
          return !!Object.keys(this.currency).length;
        },
    },
  methods: {
        clearPrice () {
          this.$emit('update:currency', {})
        },
    }
}
</script>