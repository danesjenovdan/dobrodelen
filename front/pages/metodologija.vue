<template>
  <div class="content">
    <intro-text
      lead="Metodologija za pregled transparentnosti slovenskih nevladnih organizacij "
    />
    <div class="faq">
      <div class="accordion">
        <div
          v-for="(item, i) in items"
          :id="`accordion-item-${i}`"
          :key="`accordion-item-${i}`"
          class="card"
        >
          <div
            :id="`accordion-item-heading-${i}`"
            class="card-header position-relative"
          >
            <h2 class="mb-0">
              <button
                :class="[
                  'btn',
                  'stretched-link',
                  'text-left',
                  { collapsed: item.collapsed },
                ]"
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
            :class="[
              'accordion-item-content',
              'collapse',
              { show: !item.collapsed },
            ]"
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
import uvod from '~/assets/metodologija/0_uvod.inc.html?raw';
import postopek from '~/assets/metodologija/1_postopek.inc.html?raw';
import sklop1 from '~/assets/metodologija/sklop1.inc.html?raw';
import sklop2 from '~/assets/metodologija/sklop2.inc.html?raw';
import sklop3 from '~/assets/metodologija/sklop3.inc.html?raw';
import sklop4 from '~/assets/metodologija/sklop4.inc.html?raw';
import sklop5 from '~/assets/metodologija/sklop5.inc.html?raw';

export default {
  components: {
    IntroText,
  },
  data() {
    return {
      items: [
        {
          collapsed: true,
          headerHTML: '<strong>UVOD V METODOLOGIJO</strong>',
          contentHTML: uvod,
        },
        {
          collapsed: true,
          headerHTML:
            '<strong>POSTOPEK PREGLEDA IN SISTEM OCENJEVANJA</strong>',
          contentHTML: postopek,
        },
        {
          collapsed: true,
          headerHTML:
            'SKLOP 1: <strong>DOSTOPNOST OSNOVNIH INFORMACIJ</strong>',
          contentHTML: sklop1,
        },
        {
          collapsed: true,
          headerHTML: 'SKLOP 2: <strong>DOSTOPNOST VSEBINSKIH POROČIL</strong>',
          contentHTML: sklop2,
        },
        {
          collapsed: true,
          headerHTML: 'SKLOP 3: <strong>FINANČNA TRANSPARENTNOST</strong>',
          contentHTML: sklop3,
        },
        {
          collapsed: true,
          headerHTML: 'SKLOP 4: <strong>ZBIRANJE DONACIJSKIH SREDSTEV</strong>',
          contentHTML: sklop4,
        },
        {
          collapsed: true,
          headerHTML:
            'SKLOP 5: <strong>DOSTOPNOST OBJAVLJENIH INFORMACIJ</strong>',
          contentHTML: sklop5,
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
        itemContentElement.removeEventListener(
          'transitionend',
          onTransitionEnd,
        );

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

            :deep(span) {
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

        :deep(.card-body) {
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

          strong,
          a {
            font-weight: 400;
          }

          em {
            font-weight: 400;
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
              background-image: url('~/assets/svg/arrow-list.svg');
              background-repeat: no-repeat;
              background-position: top 0.3em left;
              background-size: 1em 1em;
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
