<template>
  <header>
    <nav>
      <nuxt-link :to="{ name: 'index' }" class="nav-link">organizacije</nuxt-link>
      <h1>
        <hr />
        <nuxt-link :to="{ name: 'index' }" class="title-link">dobrodelen.si</nuxt-link>
        <hr />
      </h1>
      <nuxt-link :to="{ name: 'org-add' }" class="nav-link">prijava</nuxt-link>
    </nav>
  </header>
</template>

<style lang="scss" scoped>
header {
  margin: 2em 0;

  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1rem;
    font-weight: 600;

    .nav-link {
      flex: 1;
      text-transform: uppercase;
      font-size: 1em;
      line-height: 1;
      letter-spacing: 0.2em;
      text-align: center;
      text-decoration: none;
    }

    h1 {
      flex: 2;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0;
      text-transform: uppercase;
      font-size: 1.5em;
      font-weight: 700;
      line-height: 1;
      letter-spacing: 0.25em;
      color: orange;

      hr {
        margin: 0 0.75em;
        border: none;
        width: 4em;
        height: 0.25em;
        background: linear-gradient(to right, lightblue 25%, orange);

        &:last-of-type {
          transform: rotate(180deg);
        }
      }

      .title-link {
        text-align: center;
        transform: translateY(-10%);
        color: inherit;
        text-decoration: none;
      }
    }
  }
}
</style>
