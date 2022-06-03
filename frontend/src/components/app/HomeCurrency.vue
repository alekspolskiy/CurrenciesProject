<template>
    <div class="col s12 m6 l8">
          <div class="card-header">
            <h3>Currencies</h3>
          </div>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Expand
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <table class="orange darken-3 white-text">
                <thead>
                <tr>
                  <th>Currency</th>
                  <th>ISO</th>
                  <th>Price</th>
                </tr>
                </thead>

                <tbody v-if="lastCurrencies">
                <tr v-for="currency in lastCurrencies" :key="currency.currency_id">
                  <td>
                    <v-btn @click="displayCurrency(currency)">{{ currency.currency_name }} </v-btn>
                  </td>
                  <td>{{ currency.currency_iso }}</td>
                  <td>
                    <v-btn @click="displayPrice(currency)"> {{ currency.price }} </v-btn>
                  </td>
                </tr>
                </tbody>
              </table>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

      <div data-app>
        <CurrencyModal :currency.sync="currencyInfo" />
        <PriceModal :currency.sync="priceInfo" />
      </div>
    </div>

</template>

<script>
import {mapGetters} from "vuex"
import CurrencyModal from "@/components/app/currency/CurrencyModal";
import PriceModal from "@/components/app/currency/PriceModal";

export default {
  name: "HomeCurrency",
  data: () => ({
    currencyInfo: {},
    priceInfo: {}
  }),
  components: { CurrencyModal, PriceModal },
  computed: {
    ...mapGetters({lastCurrencies: 'getLastCurrencies'})
  },
  async mounted() {
    await this.$store.dispatch('startListener')
  },
  async beforeUnmount() {
    await this.$store.dispatch('stopListener')
  },
  methods: {
    displayCurrency(currency) {
            this.currencyInfo = currency
      },
    displayPrice(currency) {
            this.priceInfo = currency
      }
    }
}
</script>

<style scoped>

</style>