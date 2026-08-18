<template>
  <div>
    <div class="container-fluid">
      <div class="page">
        <page-header />
        <slot />
      </div>
    </div>
    <footer class="footer">
      <div class="row">
        <div class="col-12 col-lg-6 mb-3 mb-lg-0 cnvos-col">
          <div class="text-center">
            <a
              href="https://www.cnvos.si/"
              target="_blank"
              rel="noopener"
              class="mr-4"
            >
              <img
                src="/img/cnvos-logo-hires-text.png"
                alt="cvnos logo"
                class="cnvos-logo"
              />
            </a>
          </div>
          <div class="text-center social-col">
            <a
              href="https://www.facebook.com/cnvos?locale=sl_SI"
              target="_blank"
              rel="noopener"
              class="social-link"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 666.667 664.225"
              >
                <path
                  d="M666.667 333.333C666.667 149.24 517.428 0 333.333 0 149.24 0 0 149.239 0 333.333 0 489.66 107.62 620.83 252.808 656.851V435.195h-68.736V333.333h68.736v-43.892c0-113.456 51.344-166.042 162.73-166.042 21.118 0 57.557 4.14 72.463 8.281v92.339c-7.868-.828-21.532-1.243-38.509-1.243-54.657 0-75.776 20.704-75.776 74.533v36.024h108.879L463.89 435.195h-90.175v229.03c165.048-19.934 292.95-160.468 292.95-330.892"
                />
              </svg>
            </a>
            <a
              href="https://www.instagram.com/nevladniki/"
              target="_blank"
              rel="noopener"
              class="social-link"
            >
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
                <path
                  d="M292.92 3.5c-53.2 2.51-89.53 11-121.29 23.48-32.87 12.81-60.73 30-88.45 57.82s-44.79 55.7-57.51 88.62c-12.31 31.83-20.65 68.19-23 121.42S-.2 365.18.06 500.96.92 653.76 3.5 707.1c2.54 53.19 11 89.51 23.48 121.28 12.83 32.87 30 60.72 57.83 88.45s55.69 44.76 88.69 57.5c31.8 12.29 68.17 20.67 121.39 23s70.35 2.87 206.09 2.61 152.83-.86 206.16-3.39 89.46-11.05 121.24-23.47c32.87-12.86 60.74-30 88.45-57.84s44.77-55.74 57.48-88.68c12.32-31.8 20.69-68.17 23-121.35 2.33-53.37 2.88-70.41 2.62-206.17s-.87-152.78-3.4-206.1-11-89.53-23.47-121.32c-12.85-32.87-30-60.7-57.82-88.45s-55.74-44.8-88.67-57.48c-31.82-12.31-68.17-20.7-121.39-23S634.83-.2 499.04.06 346.25.9 292.92 3.5m5.84 903.88c-48.75-2.12-75.22-10.22-92.86-17-23.36-9-40-19.88-57.58-37.29s-28.38-34.11-37.5-57.42c-6.85-17.64-15.1-44.08-17.38-92.83-2.48-52.69-3-68.51-3.29-202s.22-149.29 2.53-202c2.08-48.71 10.23-75.21 17-92.84 9-23.39 19.84-40 37.29-57.57s34.1-28.39 57.43-37.51c17.62-6.88 44.06-15.06 92.79-17.38 52.73-2.5 68.53-3 202-3.29s149.31.21 202.06 2.53c48.71 2.12 75.22 10.19 92.83 17 23.37 9 40 19.81 57.57 37.29s28.4 34.07 37.52 57.45c6.89 17.57 15.07 44 17.37 92.76 2.51 52.73 3.08 68.54 3.32 202s-.23 149.31-2.54 202c-2.13 48.75-10.21 75.23-17 92.89-9 23.35-19.85 40-37.31 57.56s-34.09 28.38-57.43 37.5c-17.6 6.87-44.07 15.07-92.76 17.39-52.73 2.48-68.53 3-202.05 3.29s-149.27-.25-202-2.53m407.6-674.61a60 60 0 1 0 59.88-60.1 60 60 0 0 0-59.88 60.1M243.27 500.5c.28 141.8 115.44 256.49 257.21 256.22S757.02 641.3 756.75 499.5 641.29 242.98 499.5 243.26 243 358.72 243.27 500.5m90.06-.18a166.67 166.67 0 1 1 167 166.34 166.65 166.65 0 0 1-167-166.34"
                />
              </svg>
            </a>
          </div>
        </div>
        <div class="col-12 col-lg-6 partners-col">
          <div class="text-center">
            <a
              href="https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/"
              target="_blank"
              rel="noopener"
            >
              <img
                src="/img/mnzju_export.png"
                alt="mnzju logo"
                class="mju-logo"
              />
            </a>
            <a href="https://si.usembassy.gov/" target="_blank" rel="noopener">
              <img
                src="/img/usembassy.png"
                alt="us embassy logo"
                class="use-logo"
              />
            </a>
          </div>
          <div class="text-center">
            <div class="partners-text">
              K nastanku spletnega mesta Dobrodelen.si sta pripomogla
              Ministrstvo za notranje zadeve in javno upravo Republike Slovenije ter U.S. Embassy
              Ljubljana
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';

export default {
  components: {
    PageHeader,
  },
  watch: {
    $route() {
      // TODO: this.$nuxt.$emit('toggle-menu', false);
    },
  },
};
</script>

<style lang="scss" scoped>
.container-fluid {
  padding-left: 3.5rem;
  padding-right: 3.5rem;
  max-width: 1920px;

  @include media-breakpoint-down(sm) {
    padding: 0 1rem;
  }
}

.footer {
  background-color: rgba($blue, 0.1);
  padding: 2rem 3.5rem;

  @include media-breakpoint-down(sm) {
    padding: 1rem 1rem;
  }

  a {
    display: inline-block;
    padding: 5px;
  }

  .cnvos-col {
    display: flex;
    gap: 1rem;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    .cnvos-logo {
      height: 56px;

      @include media-breakpoint-down(xs) {
        height: 36px;
      }
    }

    .social-col {
      display: flex;
      justify-content: center;
      align-items: center;

      .social-link {
        display: inline-block;
        margin-right: 1rem;

        @include media-breakpoint-down(xs) {
          margin-right: 0.5rem;
        }

        &:last-child {
          margin-right: 0;
        }

        svg {
          width: 36px;
          height: 36px;

          @include media-breakpoint-down(xs) {
            width: 24px;
            height: 24px;
          }
        }
      }
    }
  }

  .partners-col {
    display: flex;
    gap: 0.5rem;
    flex-direction: column;

    .mju-logo {
      mix-blend-mode: multiply;
      margin-right: 1rem;
      height: 56px;

      @include media-breakpoint-down(xs) {
        height: 48px;
      }
    }

    .use-logo {
      height: 56px;

      @include media-breakpoint-down(xs) {
        height: 48px;
      }
    }

    .partners-text {
      margin: 0 auto;
      max-width: 420px;
      font-size: 12px;
      line-height: 1.2;
    }
  }
}
</style>
