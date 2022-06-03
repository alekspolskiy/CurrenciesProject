<template>
    <v-dialog
        v-if="showCurrency"
        v-model="showCurrency"
        persistent
        max-width="1200px"
    >
      <v-card class="text-center">
            <v-card-title class="text-h5 grey lighten-2">
                <p>
                  Currency: {{currency.currency_name}} <br>
                  Currency ISO: {{currency.currency_iso}} <br>
                  Current price: {{currency.price}}
                </p>
            </v-card-title>
        <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="red"
                    plain
                    @click="clearCurrency()"
                >
                    Close
                </v-btn>
            </v-card-actions>
      </v-card>
    </v-dialog>

</template>

<script>

export default {
    name: "CurrencyModal",
    props: ['currency'],
    data(){
        return {

        }
    },
    computed: {
        showCurrency: function() {
            return !!Object.keys(this.currency).length;
        }
    },
    methods: {
        clearCurrency () {
            this.$emit('update:currency', {})
        }
    }
}
</script>