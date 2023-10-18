<template>
  <div class="error-container">
    <h1>Napaka 😢</h1>
    <p>Prišlo je do napake pri nalaganju strani.</p>
  </div>
</template>

<script>
definePageMeta({ layout: 'landing' });
</script>

<style lang="scss" scoped>
.error-container {
  position: relative;
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: #000;
  z-index: 0;

  &::before {
    content: 'ERROR';
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    inset: 0;
    z-index: -1;
    font-size: calc(28 * 1vw);
    font-weight: 900;
    color: #fff;
    line-height: 1;

    @media (max-width: 768px) {
      align-items: flex-start;
    }
  }

  h1 {
    margin-bottom: 1rem;
    font-size: 3rem;
    font-weight: 700;

    @media (max-width: 768px) {
      font-size: 2rem;
    }
  }

  p {
    font-size: 1.5rem;
    margin-bottom: 0;

    @media (max-width: 768px) {
      font-size: 1rem;
    }
  }
}
</style>
