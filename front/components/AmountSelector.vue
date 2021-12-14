<template>
  <div class="amount-selector">
    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <button
          v-for="presetAmount in presetAmounts"
          :key="presetAmount"
          :class="[
            'btn',
            'btn-outline-primary',
            {
              active: isSelectedAmount(presetAmount),
              focus: isSelectedAmount(presetAmount),
            },
          ]"
          type="button"
          @click.prevent="selectAmount(presetAmount)"
        >
          {{ presetAmount }} €
        </button>
      </div>
      <input
        v-model="customAmount"
        type="text"
        class="form-control"
        placeholder="Poljubno"
        @input="selectCustomAmount"
      />
      <div class="input-group-append">
        <span class="input-group-text">€</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      presetAmounts: [5, 25, 50],
      amount: 5,
      customAmount: '',
      customValueSelected: false,
    };
  },
  mounted() {
    this.$emit('change', this.amount);
  },
  methods: {
    isSelectedAmount(value) {
      return !this.customValueSelected && this.amount === value;
    },
    selectAmount(value) {
      this.amount = value;
      this.customValueSelected = false;
      this.$emit('change', this.amount);
    },
    selectCustomAmount(event) {
      const formattedValue = parseInt(event.target.value, 10);
      if (isNaN(formattedValue)) {
        this.customAmount = '';
      } else {
        this.customAmount = formattedValue;
        this.customValueSelected = true;
        this.$emit('change', this.customAmount);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.amount-selector {
  margin: 0 auto;
  max-width: 280px;

  input {
    text-align: right;
  }
}
</style>
