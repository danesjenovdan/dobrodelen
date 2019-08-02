<template>
  <header>
    <nav>
      <nuxt-link :to="{ name: 'org-add' }" class="nav-link text-primary">
        <span>prijava organizacije</span>
      </nuxt-link>
      <h1>
        <hr />
        <nuxt-link :to="{ name: 'organizations' }" class="title-link text-warning">
          <span>DOBRODELEN.SI</span>
        </nuxt-link>
        <hr />
      </h1>
      <nuxt-link :to="{ name: 'methodology' }" class="nav-link text-primary">
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
      font-size: 1.25rem;
      line-height: 1;
      letter-spacing: 0.2em;
      text-align: center;
      text-decoration: none;

      span {
        display: inline-block;
        position: relative;

        &::after {
          content: '';
          display: block;
          position: absolute;
          bottom: -0.07em;
          left: 0.07em;
          right: 0.17em;
          height: 0.35em;
        }
      }

      &.nuxt-link-exact-active span::after {
        background: rgba($blue, 0.3);
      }
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
        background: linear-gradient(to right, $blue 20%, $yellow);

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
