<template>
  <div class="content">
    <intro-text
      lead="Metodologija za ocenjevanje in razvrščanje slovenskih nevladnih organizacij"
    />
    <div class="faq">
      <div class="accordion">
        <div
          v-for="(item, i) in items"
          :id="`accordion-item-${i}`"
          :key="`accordion-item-${i}`"
          class="card"
        >
          <div :id="`accordion-item-heading-${i}`" class="card-header position-relative">
            <h2 class="mb-0">
              <button
                :class="['btn', 'stretched-link', 'text-left', { collapsed: item.collapsed }]"
                type="button"
                :aria-expanded="`${!item.collapsed}`"
                :aria-controls="`accordion-item-content-${i}`"
                @click="toggleItem(i)"
              >
                <!-- eslint-disable-next-line vue/no-v-html -->
                <span v-html="item.headerHTML" />
              </button>
              <i class="icon icon-arrow icon-arrow--right" />
            </h2>
          </div>
          <div
            :id="`accordion-item-content-${i}`"
            ref="accordion-item-content"
            :class="['accordion-item-content', 'collapse', { show: !item.collapsed }]"
            :aria-labelledby="`accordion-item-heading-${i}`"
          >
            <!-- eslint-disable-next-line vue/no-v-html -->
            <div class="card-body" v-html="item.contentHTML" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import IntroText from '~/components/IntroText.vue';

export default {
  components: {
    IntroText,
  },
  data() {
    return {
      items: [
        {
          collapsed: true,
          headerHTML: 'Kriterij 1: <strong>Nadzor nad poslovanjem</strong>',
          contentHTML: require('../assets/metodologija/kriterij1.inc.html').default,
        },
        {
          collapsed: true,
          headerHTML: 'Kriterij 2: <strong>Strateško načrtovanje organizacij</strong>',
          contentHTML: require('../assets/metodologija/kriterij2.inc.html').default,
        },
        {
          collapsed: true,
          headerHTML: 'Kriterij 3: <strong>Finančno upravljanje</strong>',
          contentHTML: require('../assets/metodologija/kriterij3.inc.html').default,
        },
        {
          collapsed: true,
          headerHTML: 'Kriterij 4: <strong>Transparentnost organizacij</strong>',
          contentHTML: require('../assets/metodologija/kriterij4.inc.html').default,
        },
        {
          collapsed: true,
          headerHTML: '<strong>Skupna ocena</strong>',
          contentHTML: require('../assets/metodologija/skupnaocena.inc.html').default,
        },
      ],
    };
  },
  methods: {
    toggleItem(i) {
      const itemContentElement = this.$refs['accordion-item-content'][i];

      let from = `${itemContentElement.firstElementChild.clientHeight}px`;
      let to = '0px';
      if (!itemContentElement.classList.contains('show')) {
        [from, to] = [to, from];
      }

      itemContentElement.style.height = from;
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          itemContentElement.style.height = to;
        });
      });

      const onTransitionEnd = () => {
        itemContentElement.style.height = '';
        itemContentElement.removeEventListener('transitionend', onTransitionEnd);

        this.items = this.items.map((item, index) => ({
          ...item,
          collapsed: i === index ? !item.collapsed : item.collapsed,
        }));
      };
      itemContentElement.addEventListener('transitionend', onTransitionEnd);
    },
  },
  head() {
    return {
      title: 'Metodologija',
    };
  },
};
</script>

<style lang="scss" scoped>
.content {
  margin-bottom: 5rem;

  .faq {
    .card {
      border: 0;

      & + .card {
        margin-top: 1.5rem;
      }

      .card-header {
        padding: 3rem 3.5rem;
        background: #f6f2f0;
        border: 0;

        @include media-breakpoint-down(sm) {
          padding: 1rem;
        }

        h2 {
          display: flex;
          align-items: center;
          justify-content: space-between;

          button {
            font-size: 1.85rem;
            color: inherit;

            @include media-breakpoint-down(sm) {
              font-size: 1.25rem;
            }

            /deep/ span {
              font-weight: 300;
              letter-spacing: 0.2em;

              strong {
                font-weight: 600;
                text-transform: uppercase;
              }
            }
          }

          .icon {
            margin: 0.375rem 0.75rem;
            transition: transform 0.15s ease;
          }

          button[aria-expanded='true'] + .icon {
            transform: rotate(90deg);
          }
        }
      }

      .accordion-item-content {
        transition: height 1s ease;

        &.collapse:not(.show) {
          display: block;
          height: 0;
        }

        /deep/ .card-body {
          padding-top: 4rem;
          padding-bottom: 4rem;
          font-size: 1.5rem;
          margin: 0 14rem;
          font-weight: 300;
          line-height: 1.4;

          @include media-breakpoint-down(sm) {
            margin: 0;
            padding: 1rem;
            font-size: 1rem;
          }

          strong {
            font-weight: 400;
          }

          em {
            font-weight: 600;
            font-style: italic;
          }

          p {
            margin-bottom: 0;

            & + p {
              margin-top: 2rem;

              @include media-breakpoint-down(sm) {
                margin-top: 1rem;
              }
            }

            & + ul {
              margin-top: 0.5rem;
            }

            & + table,
            & + .table,
            & + .table-responsive {
              margin-top: 0.75rem;
            }
          }

          ul {
            margin-bottom: 2rem;
            list-style: none;
            padding-left: 2.5rem;

            @include media-breakpoint-down(sm) {
              padding-left: 1rem;
            }

            li {
              padding-left: 1.4em;
              background-image: url('~assets/svg/arrow-list.svg');
              background-repeat: no-repeat;
              background-position: top 0.38em left;
              background-size: 1em;
            }
          }

          table {
            margin-bottom: 2rem;
            font-size: 1.25rem;

            @include media-breakpoint-down(sm) {
              margin-bottom: 1rem;
              font-size: 1rem;
            }

            td {
              border: 1px solid $blue;
              padding: 0.5rem 1.5rem;
            }
          }
        }
      }
    }
  }
}
</style>
