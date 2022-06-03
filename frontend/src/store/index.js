import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


let eventSource = ''

export default new Vuex.Store({  state: {
    currencies: []
  },
  getters: {
    getLastCurrencies(state){
      return state.currencies[state.currencies.length - 1]
    },
    getPriceByCurrency: (state) => (id) => {
          return state.currencies.map(highItem => {
            return highItem.find(currency => currency.currency_id === id).price
        })
    }
  },
  mutations: {
    SET_CURRENCIES(state, payload){
      state.currencies.push(payload)
    }
  },
  actions: {
    startListener: ({commit}) => {
        eventSource = new EventSource('http://localhost:8000/api/v1/exchange/start')
        eventSource.onmessage = function (e) {
          commit("SET_CURRENCIES", JSON.parse(e.data))
        }
    },
    stopListener() {
      eventSource.close()
    },
  },
  modules: {
  }
})
