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
        <button class="menu-button btn icon icon-menu d-md-none">
          <span class="sr-only">menu</span>
        </button>
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

  @include media-breakpoint-down(sm) {
    margin: 1rem 0;
  }

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

      @include media-breakpoint-down(sm) {
        display: none;
      }

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

      @include media-breakpoint-down(sm) {
        font-size: 1.5rem;
        flex: 1 0 0%;
      }

      hr {
        margin: 0;
        border: none;
        width: 3.4em;
        height: 0.2em;
        background: linear-gradient(to right, $blue 20%, $yellow);
        // transformed elements are antialiased differently
        // used for consistency with the opposite one that is rotated 180deg
        transform: rotate(360deg);

        @include media-breakpoint-down(sm) {
          width: auto;
          flex: 1 1 0%;
          display: none;
        }

        &:last-of-type {
          transform: rotate(180deg);

          @include media-breakpoint-down(sm) {
            display: block;
          }
        }
      }

      .title-link {
        text-align: center;
        color: inherit;
        text-decoration: none;
        margin: 0 0.65em 0 0.85em;

        @include media-breakpoint-down(sm) {
          margin-left: 0.2rem;
          margin-right: 0.6rem;
        }
      }

      .menu-button {
        // position: absolute;
        // top: 0.75rem;
        // right: 0.75rem;
        width: 2rem;
        height: 2rem;
        padding: 0;
        background-size: 75% 75%;
        border-radius: 50%;
        margin-left: 0.2rem;
        margin-right: -0.5rem;
        // background-color: #f6f2f0;
      }
    }
  }
}
</style>
