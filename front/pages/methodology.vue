<template>
  <div class="content">
    <intro-text
      lead="Metodologija za ocenjevanje in razvrščanje slovenskih nevladnih organizacij"
      text="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse."
    />
    <div class="faq">
      <div class="accordion">
        <div
          v-for="(item, i) in items"
          :id="`accordion-item-${i}`"
          :key="`accordion-item-${i}`"
          class="card"
        >
          <div :id="`accordion-item-heading-${i}`" class="card-header">
            <h2 class="mb-0">
              <button
                :class="['btn', { collapsed: item.collapsed }]"
                type="button"
                :aria-expanded="`${!item.collapsed}`"
                :aria-controls="`accordion-item-content-${i}`"
                @click="toggleItem(i)"
              >
                <span>
                  Kriterij 1:
                  <strong>Nadzor nad poslovanjem</strong>
                </span>
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
            <div class="card-body">
              <p>
                <strong>
                  Organizacija dosega strateške cilje organizacije (strateški cilji postavljeni,
                  napredek se spremlja vsaj na 2 leti, obstajajo poročila o napredku).
                </strong>
              </p>
              <p>
                Poleg letnega načrta dela ima organizacija tudi strateške oziroma dolgoročne cilje,
                ki usmerjajo njeno delo in aktivnosti proti uresničevanju njenega poslanstva. Pri
                tem samo poimenovanje dokumenta ni pomembno, tudi kakovost dokumenta se ne točkuje.
                V tej fazi je pomembno le to, da ima organizacija dolgoročne načrte in cilje in da
                se jih trudi uresničevati.
              </p>
              <p>Podatki, ki jih pri tem organizacije posredujejo:</p>
              <ul>
                <li>opredelitev, ali organizacija strateško načrtuje,</li>
                <li>predložitev strateškega načrta, če ga ima,</li>
                <li>
                  opredelitev, ali organizacija spremlja doseganje strateških ciljev in predložitev
                  poročila, če obstaja.
                </li>
              </ul>
              <p>
                <strong>Točkovnik</strong>
              </p>
              <p>2.1 - organizacija ima strateški načrt</p>
              <table>
                <tbody>
                  <tr>
                    <td>
                      <strong>da</strong>
                    </td>
                    <td>
                      <strong>2 točki</strong>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <strong>ne</strong>
                    </td>
                    <td>
                      <strong>0 točk</strong>
                    </td>
                  </tr>
                </tbody>
              </table>
              <p>2.2 - organizacija spremlja doseganje strateškega načrta</p>
              <table>
                <tbody>
                  <tr>
                    <td>
                      <strong>da</strong>
                    </td>
                    <td>
                      <strong>2 točki</strong>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <strong>ne</strong>
                    </td>
                    <td>
                      <strong>0 točk</strong>
                    </td>
                  </tr>
                </tbody>
              </table>
              <p>
                2.3 - organizacija pripravlja poročila o spremljanju napredka pri doseganju
                strateških ciljev
              </p>
              <table>
                <tbody>
                  <tr>
                    <td>
                      <strong>da</strong>
                    </td>
                    <td>
                      <strong>2 točki</strong>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <strong>ne</strong>
                    </td>
                    <td>
                      <strong>0 točk</strong>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
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
        },
        {
          collapsed: true,
        },
        {
          collapsed: true,
        },
        {
          collapsed: true,
        },
        {
          collapsed: true,
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

        h2 {
          display: flex;
          align-items: center;
          justify-content: space-between;

          button {
            font-size: 1.85rem;
            color: inherit;

            span {
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

        .card-body {
          padding-top: 4rem;
          padding-bottom: 4rem;
          font-size: 1.5rem;
          margin: 0 14rem;
          font-weight: 300;
          line-height: 1.4;

          strong {
            font-weight: 600;
          }

          p {
            margin-bottom: 0;

            & + p {
              margin-top: 2rem;
            }

            & + ul {
              margin-top: 0.5rem;
            }

            & + table {
              margin-top: 0.75rem;
            }
          }

          ul {
            margin-bottom: 2rem;
            list-style: none;

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

            td {
              border: 1px solid $blue;
              padding: 0.5rem 3rem;
            }
          }
        }
      }
    }
  }
}
</style>
