<template>
  <div class="form-stages">
    <div class="stage active">Osnovni podatki</div>
    <div class="stage">Poslanstvo</div>
    <div class="stage">Lorem ipsum</div>
    <div class="stage">dolor, sit amet</div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.form-stages {
  display: flex;
  margin-left: -0.5rem;
  margin-right: -0.5rem;

  .stage {
    flex: 1;
    position: relative;
    text-align: center;
    padding-bottom: 1.5rem;
    font-size: 0.9375rem;

    &::after {
      content: '';
      display: block;
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      height: 0.75rem;
      background: $blue;
      margin: 0 0.5rem;
      opacity: 0.3;
    }

    &.active {
      color: $blue;

      &::after {
        opacity: 1;
      }
    }
  }
}
</style>
