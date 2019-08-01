<template>
  <header>
    <nav>
      <nuxt-link :to="{ name: 'org-add' }" class="nav-link text-secondary">
        <span>prijava organizacije</span>
      </nuxt-link>
      <h1>
        <hr />
        <nuxt-link :to="{ name: 'index' }" class="title-link text-primary">DOBRODELEN.SI</nuxt-link>
        <hr />
      </h1>
      <nuxt-link :to="{ name: 'methodology' }" class="nav-link text-secondary">
        <span>metodologija</span>
      </nuxt-link>
    </nav>
  </header>
</template>

<style lang="scss" scoped>
header {
  margin: 3.5em 0;

  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1rem;
    font-weight: 600;

    .nav-link {
      flex: 1;
      text-transform: uppercase;
      font-size: 1.5rem;
      line-height: 1;
      letter-spacing: 0.2em;
      text-align: center;
      text-decoration: none;
    }

    h1 {
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0;
      text-transform: uppercase;
      font-size: 2.5rem;
      font-weight: 700;
      line-height: 1;
      letter-spacing: 0.2em;

      hr {
        margin: 0;
        border: none;
        width: 3.4em;
        height: 0.2em;
        background: linear-gradient(to right, $secondary 20%, $primary);

        &:last-of-type {
          transform: rotate(180deg);
        }
      }

      .title-link {
        text-align: center;
        color: inherit;
        text-decoration: none;
        margin: 0 0.65em 0 0.85em;
      }
    }
  }
}
</style>
