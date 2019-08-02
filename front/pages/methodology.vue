<template>
  <div class="content">
    <intro-text
      lead="Metodologija za ocenjevanje in razvrščanje slovenskih nevladnih organizacij"
      text="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse."
    />
    <div class="faq">
      <div class="accordion">
        <div class="card">
          <div class="card-header">
            <h2 class="mb-0">
              <button class="btn" type="button" aria-expanded="false" aria-controls="collapseOne">
                <span>
                  Kriterij 1:
                  <strong>Nadzor nad poslovanjem</strong>
                </span>
              </button>
              <i class="icon icon-arrow icon-arrow--right" />
            </h2>
          </div>
          <div id="collapseOne" class="collapse" aria-labelledby="headingOne">
            <div class="card-body">
              <p>
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
                richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor
                brunch. Food truck quinoa nesciunt laborum eiusmod.
              </p>
              <p>
                Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee
                nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes
                anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo.
                Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you
                probably haven't heard of them accusamus labore sustainable VHS.
              </p>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header">
            <h2 class="mb-0">
              <button class="btn" type="button" aria-expanded="true" aria-controls="collapseOne">
                <span>
                  Kriterij 1:
                  <strong>Nadzor nad poslovanjem</strong>
                </span>
              </button>
              <i class="icon icon-arrow icon-arrow--right" />
            </h2>
          </div>
          <div id="collapseOne" class="collapse show" aria-labelledby="headingOne">
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
        <div class="card">
          <div class="card-header">
            <h2 class="mb-0">
              <button class="btn" type="button" aria-expanded="false" aria-controls="collapseOne">
                <span>
                  Kriterij 1:
                  <strong>Nadzor nad poslovanjem</strong>
                </span>
              </button>
              <i class="icon icon-arrow icon-arrow--right" />
            </h2>
          </div>
          <div id="collapseOne" class="collapse" aria-labelledby="headingOne">
            <div class="card-body">
              <p>
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
                richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor
                brunch. Food truck quinoa nesciunt laborum eiusmod.
              </p>
              <p>
                Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee
                nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes
                anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo.
                Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you
                probably haven't heard of them accusamus labore sustainable VHS.
              </p>
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
};
</script>

<style lang="scss" scoped>
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
</style>
