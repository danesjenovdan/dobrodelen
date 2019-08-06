<template>
  <div class="content">
    <div class="row">
      <div class="col-12">
        <div class="org-title-container text-center">
          <img
            src="~/assets/placeholder.png"
            alt="organization placeholder image"
            class="rounded-circle bg-dark mb-4"
          />
          <h2>{{ organization.name }}</h2>
          <div class="stars" @click="toggleModal(true)">
            <i
              v-for="i in 5"
              :key="i"
              :class="['icon', 'icon-star', { 'icon-star--full': organization.stars >= i }]"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-6">
        <div class="org-info">
          <dl class="row">
            <dt class="col-4">Druga imena</dt>
            <dd class="col-8">{{ organization.name }}</dd>
            <dt class="col-4">Kontakt</dt>
            <dd class="col-8">
              <div>Ime</div>
              <div>Naslov</div>
              <div>email</div>
              <div>telefon</div>
            </dd>
            <dt class="col-4">Spletno mesto</dt>
            <dd class="col-8">website.com</dd>
            <dt class="col-4">Družbena omrežja</dt>
            <dd class="col-8">ikone</dd>
            <dt class="col-4">Področje delovanja</dt>
            <dd class="col-8">človekove pravice, demokracija in enakost</dd>
          </dl>
        </div>
        <div class="org-info">
          <dl class="row">
            <dt class="col-9">Povprečni letni proračun v zadnjih treh letih</dt>
            <dd class="col-3">1 000 000</dd>
            <dt class="col-9">Število zaposlenih v zadnjem zaključenem letu</dt>
            <dd class="col-3">1</dd>
            <dt class="col-9">Organizacija ima status humanitarne organizacije</dt>
            <dd class="col-3">DA</dd>
            <dt class="col-9">etc.</dt>
            <dd class="col-3">...</dd>
          </dl>
        </div>
      </div>
      <div class="col-6">
        <div class="org-description">
          <h4>Poslanstvo</h4>
          <!-- eslint-disable prettier/prettier -->
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic, numquam. Optio rem modi
            animi nisi exercitationem, pariatur quasi architecto harum? Voluptatem assumenda
            reiciendis itaque nihil, reprehenderit cum dignissimos sint nisi. Sapiente sunt
            consequatur totam atque quas quos porro et, voluptate nam non tempore? Non, illo cum iste
            fuga corrupti distinctio ex nesciunt at ipsum vitae sed quibusdam tenetur nihil suscipit.
            Alias explicabo non optio exercitationem fuga doloremque? Accusamus cumque neque facilis
            quasi aliquid velit ad repellendus veniam iusto, atque voluptates architecto dolorem
            adipisci impedit dignissimos, corrupti perspiciatis. Libero, esse iste.
          </p>
          <h4>Opis</h4>
          <p>
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Architecto aliquam adipisci
            placeat enim illum sunt voluptas maiores. Qui, rerum nulla. Dolor odio aut vel similique
            eaque consequatur voluptates deserunt alias? Similique obcaecati ullam neque? Voluptatum
            corporis similique nulla magni labore commodi nam quibusdam laborum consequatur. Omnis qui
            unde iste? Quidem pariatur beatae vero ullam perspiciatis? Maiores, voluptates? Ipsam,
            expedita odio. Consequuntur temporibus perferendis quia sit pariatur repellendus corrupti
            illum enim? Eaque eveniet perspiciatis tempore ratione delectus. Temporibus, quibusdam, a
            soluta eveniet doloribus asperiores cum, atque consequuntur iusto tempore voluptates modi.
            Aut hic iusto ut explicabo exercitationem atque possimus ex, eveniet facere libero
            consequatur at. Quisquam quasi similique temporibus adipisci? Officia ducimus eveniet
            maiores reiciendis quasi alias veniam eius iusto possimus?
          </p>
          <p>
            Voluptate ducimus tempore
            laboriosam in nihil laudantium tempora eos sed voluptates impedit neque eligendi iure,
            aliquid consequatur delectus asperiores ipsum ullam! Cupiditate placeat minima dolor atque
            neque culpa iste explicabo! Pariatur sapiente voluptate voluptatum ut, possimus repellat
            earum itaque autem laboriosam cupiditate omnis facere quod incidunt magni ex blanditiis
            voluptates tenetur dolor rerum, beatae quam necessitatibus architecto. Laudantium, sequi
            asperiores! Alias, aliquam laborum. Reprehenderit quasi optio architecto cumque eaque
            itaque, animi, numquam quas impedit dolores atque accusamus odit. Dolorem quam labore nisi
            et cumque deserunt veniam exercitationem quisquam eligendi animi? Voluptatem quae ullam
            distinctio. Modi accusamus consectetur, perferendis facilis dicta aliquid itaque quis
            repellat ad fugit aut obcaecati quas hic possimus voluptate dolorum, quos debitis libero
            animi autem quibusdam nobis. Dolores corporis, numquam suscipit ut possimus itaque
            expedita vel consectetur deleniti error illo modi dicta earum molestias aliquam quaerat
            aperiam nulla, rem officiis ipsa nam natus et non? Harum, velit. Magnam sed laborum
            recusandae ratione nisi adipisci temporibus quisquam architecto voluptatibus accusamus,
            dolore doloremque quasi tenetur sint aut facilis ipsum obcaecati dolores hic quidem. Eius
            odit amet omnis facilis odio!
          </p>
          <!-- eslint-enable prettier/prettier -->
        </div>
      </div>
    </div>

    <transition name="fade-modal">
      <div
        v-if="showStarsModal"
        class="modal show"
        tabindex="-1"
        role="dialog"
        style="display:block"
      >
        <div
          class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable"
          role="document"
        >
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Skupna ocena</h5>
              <div class="stars">
                <i
                  v-for="i in 5"
                  :key="i"
                  :class="['icon', 'icon-star', { 'icon-star--full': organization.stars >= i }]"
                />
              </div>
              <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
                @click="toggleModal(false)"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <p>
                Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget
                dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
                nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium
                quis, sem. Nulla consequat massa quis enim.
              </p>
              <table class="table">
                <tbody>
                  <tr>
                    <td>Število zaposlenih v zadnjem zaključenem letu</td>
                    <td>1</td>
                  </tr>
                  <tr>
                    <td>Število zaposlenih v zadnjem zaključenem letu</td>
                    <td>1</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade-backdrop">
      <div v-if="showStarsModal" class="modal-backdrop show" />
    </transition>
  </div>
</template>

<script>
export default {
  validate({ params }) {
    return /^\d+$/.test(params.id);
  },
  data() {
    return {
      showStarsModal: false,
    };
  },
  async asyncData({ $axios, params, query }) {
    const editKey = query.edit_key ? `?edit_key=${query.edit_key}` : '';
    const orgResp = await $axios.$get(
      `http://127.0.0.1:8000/api/organizations/${params.id}/${editKey}`,
    );
    return {
      organization: orgResp,
    };
  },
  beforeDestroy() {
    this.toggleModal(false);
  },
  methods: {
    toggleModal(show = !this.showStarsModal) {
      if (typeof window !== 'undefined' && document.body.classList) {
        if (show) {
          document.body.classList.add('modal-open');
        } else {
          document.body.classList.remove('modal-open');
        }
      }
      this.showStarsModal = show;
    },
  },
};
</script>

<style lang="scss" scoped>
.content {
  margin-bottom: 5rem;

  .stars {
    display: inline-block;
    margin-top: 0.75rem;

    .icon {
      margin: 0 0.3rem;
    }
  }

  .org-title-container {
    background: #f6f2f0;
    padding: 2.5rem 4.2rem;
    margin-bottom: 5rem;

    img {
      width: 100%;
      max-width: 10rem;
    }

    h2 {
      font-size: 3rem;
      font-weight: 300;
      line-height: 1.4;
      letter-spacing: 0.2em;
    }

    .stars {
      margin-top: 1.5rem;
      cursor: pointer;
    }
  }

  .org-info {
    padding: 4.2rem;
    padding-bottom: 0.7rem;
    border: 1px solid $blue;
    margin-right: 2rem;

    & + .org-info {
      margin-top: -1px;
    }

    dl {
      font-size: 1.5rem;
      line-height: 1.4;

      dt,
      dd {
        margin-bottom: 2.5rem;
      }

      dt {
        font-weight: 300;
      }

      dd {
        font-weight: 600;
      }
    }
  }

  .org-description {
    h4 {
      font-weight: 400;
      margin-bottom: 1.5rem;
      letter-spacing: 0.2em;
    }

    p {
      font-size: 1.5rem;
      font-weight: 300;
      font-style: italic;
      line-height: 1.4;
      margin-bottom: 1.5rem;
    }

    p + h4 {
      margin-top: 5rem;
    }
  }

  .modal {
    .table {
      margin-top: 4rem;

      tr {
        border-top: 1px solid $blue;

        &:last-of-type {
          border-bottom: 1px solid $blue;
        }

        td {
          border: 0;
          padding-top: 1.25rem;
          padding-bottom: 1.25rem;

          &:first-of-type {
            padding-left: 0;
          }
        }
      }
    }
  }
}

.fade-backdrop-enter-active,
.fade-backdrop-leave-active {
  transition: opacity 0.15s linear;
}

.fade-backdrop-leave-active {
  transition-delay: 0.15s;
}

.fade-backdrop-enter,
.fade-backdrop-leave-to {
  opacity: 0;
}

.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.15s linear;
}

.fade-modal-enter-active {
  transition-delay: 0.15s;
}

.fade-modal-enter,
.fade-modal-leave-to {
  opacity: 0;
}
</style>
