<template>
  <div class="content">
    <content-title
      :image="
        organization.cover_photo
          ? `${apiBaseUrl}${organization.cover_photo.url}`
          : '/img/placeholder.png'
      "
      :title="organization.name"
      :stars="organization.stars"
      @stars-click="toggleModal(true)"
    />
    <div class="row">
      <div class="col-12 col-md-6">
        <div class="org-info">
          <dl class="row">
            <dt class="col-4">Druga imena</dt>
            <dd class="col-8">{{ organization.additional_names }}</dd>
            <dt class="col-4">Kontakt</dt>
            <dd class="col-8">
              <div v-if="organization.contact_name">{{ organization.contact_name }}</div>
              <div v-if="organization.contact_email">
                <a :href="`mailto:${organization.contact_email}`" target="_blank">{{
                  organization.contact_email
                }}</a>
              </div>
              <div v-if="organization.contact_phone">
                <a :href="`tel:${organization.contact_phone}`" target="_blank">{{
                  formatPhoneNumber(organization.contact_phone)
                }}</a>
              </div>
            </dd>
            <dt class="col-4">Spletno mesto</dt>
            <dd class="col-8">
              <a :href="organization.web_page" target="_blank" rel="noopener noreferrer">{{
                organization.web_page
              }}</a>
            </dd>
            <dt class="col-4">Družbena omrežja</dt>
            <dd class="col-8">
              <a
                v-for="link in organization.links"
                :key="link"
                :href="link"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i :class="['icon', `icon-${getIconForUrl(link)}`]" />
              </a>
            </dd>
            <dt class="col-4">Področja delovanja</dt>
            <dd class="col-8">
              <div v-for="area in organization.area" :key="area">{{ area }}</div>
            </dd>
          </dl>
        </div>
        <div class="org-info">
          <dl class="row">
            <dt class="col-9">Povprečni letni proračun v zadnjih treh letih</dt>
            <dd class="col-3">{{ organization.avg_revenue }}</dd>
            <dt class="col-9">Število zaposlenih v zadnjem zaključenem letu</dt>
            <dd class="col-3">{{ organization.employed }}</dd>
            <dt class="col-9">Organizacija ima status humanitarne organizacije</dt>
            <dd class="col-3">{{ organization.is_charity ? 'DA' : 'NE' }}</dd>
            <dt class="col-9">Organizacija ima status delovanja v javnem interesu</dt>
            <dd class="col-3">{{ organization.has_public_interest ? 'DA' : 'NE' }}</dd>
            <dt class="col-9">Organizacija je vpisana v evidenco prostotovoljskih organizacij</dt>
            <dd class="col-3">{{ organization.is_voluntary ? 'DA' : 'NE' }}</dd>
            <dt class="col-9">Organizacija je na seznamu upravičencev do 0,5 % dohodnine</dt>
            <dd class="col-3">{{ organization.zero5 ? 'DA' : 'NE' }}</dd>
          </dl>
        </div>
      </div>
      <div class="col-12 col-md-6">
        <div class="org-description">
          <h4>Poslanstvo</h4>
          <!-- eslint-disable-next-line vue/no-v-html -->
          <div v-html="paragraphise(organization.mission)" />
          <h4>Opis</h4>
          <!-- eslint-disable-next-line vue/no-v-html -->
          <div v-html="paragraphise(organization.description)" />
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
import { keys } from 'lodash';
import ContentTitle from '~/components/ContentTitle.vue';
import formatPhoneNumberMixin from '~/mixins/formatPhoneNumber.js';

export default {
  components: {
    ContentTitle,
  },
  mixins: [formatPhoneNumberMixin],
  validate({ params }) {
    return /^\d+$/.test(params.id);
  },
  data() {
    return {
      apiBaseUrl: process.env.API_BASE_URL,
      showStarsModal: false,
    };
  },
  async asyncData({ $axios, params, query }) {
    const editKey = query.edit_key ? `?edit_key=${query.edit_key}` : '';
    const orgResp = await $axios.$get(`/api/organizations/${params.id}/${editKey}`);
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
    getIconForUrl(url) {
      const domains = {
        facebook: ['facebook.com', 'fb.com', 'fb.me'],
        twitter: ['twitter.com'],
        instagram: ['instagram.com'],
        youtube: ['youtube.com', 'youtu.be'],
        vimeo: ['vimeo.com'],
      };

      return keys(domains).find((key) => domains[key].some((d) => url.indexOf(d) !== -1)) || 'link';
    },
    paragraphise(text) {
      const paragraphs = text
        .trim()
        .replace(/\r\n/g, '\n')
        .replace(/\r/g, '\n')
        .split(/\n\n+/g);
      return paragraphs.map((p) => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('');
    },
  },
  head() {
    return {
      title: this.organization.name,
    };
  },
};
</script>

<style lang="scss" scoped>
.content {
  margin-bottom: 5rem;

  .org-info {
    padding: 4.2rem;
    padding-bottom: 0.7rem;
    border: 1px solid $blue;
    margin-right: 2rem;

    @include media-breakpoint-down(sm) {
      margin-right: 0;
      padding: 1.5rem;
      padding-bottom: 0;
    }

    & + .org-info {
      margin-top: -1px;
    }

    dl {
      font-size: 1.5rem;
      line-height: 1.4;

      @include media-breakpoint-down(sm) {
        font-size: 1rem;
      }

      dt,
      dd {
        margin-bottom: 2.5rem;

        @include media-breakpoint-down(sm) {
          margin-bottom: 1.25rem;
        }
      }

      dt {
        font-weight: 300;
      }

      dd {
        font-weight: 600;

        a {
          color: inherit;
        }
      }
    }
  }

  .org-description {
    @include media-breakpoint-down(sm) {
      margin-top: 2rem;
    }

    h4 {
      font-weight: 400;
      margin-bottom: 1.5rem;
      letter-spacing: 0.2em;

      @include media-breakpoint-down(sm) {
        margin-bottom: 0.5rem;
      }
    }

    /deep/ div {
      p {
        font-size: 1.5rem;
        font-weight: 300;
        font-style: italic;
        line-height: 1.4;
        margin-bottom: 1.5rem;

        @include media-breakpoint-down(sm) {
          font-size: 1.25rem;
        }
      }
    }

    div + h4 {
      margin-top: 5rem;

      @include media-breakpoint-down(sm) {
        margin-top: 2rem;
      }
    }
  }

  .modal {
    .stars {
      display: inline-block;
      margin-top: 0.75rem;

      .icon {
        margin: 0 0.3rem;
      }
    }

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
