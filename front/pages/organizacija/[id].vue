<template>
  <div class="content">
    <content-title
      :image="
        organization.cover_photo
          ? `${organization.cover_photo.full_url}`
          : '/img/placeholder.png'
      "
      :title="organization.name"
      :stars="organization.stars"
      :donation="true"
      @stars-click="toggleStarsModal(true)"
      @donate-click="toggleDonateModal(true)"
    />
    <div class="row">
      <div class="col-12 col-md-5">
        <div class="org-info">
          <dl class="row">
            <dt class="col-4">Druga imena</dt>
            <dd class="col-8">{{ organization.additional_names }}</dd>
            <dt class="col-4">Kontakt</dt>
            <dd class="col-8">
              <div v-if="organization.contact_name">
                {{ organization.contact_name }}
              </div>
              <div v-if="organization.contact_email">
                <a
                  :href="`mailto:${organization.contact_email}`"
                  target="_blank"
                  >{{ organization.contact_email }}</a
                >
              </div>
              <div v-if="organization.contact_phone">
                <a
                  :href="`tel:${organization.contact_phone}`"
                  target="_blank"
                  >{{ formatPhoneNumber(organization.contact_phone) }}</a
                >
              </div>
            </dd>
            <dt class="col-4">Spletno mesto</dt>
            <dd class="col-8">
              <a
                :href="organization.web_page"
                target="_blank"
                rel="noopener noreferrer"
                >{{ organization.web_page }}</a
              >
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
              <div v-for="area in organization.area" :key="area">
                {{ area }}
              </div>
            </dd>
            <dt class="col-4">Regije</dt>
            <dd class="col-8">
              <div v-for="region in organization.region" :key="region">
                {{ region }}
              </div>
            </dd>
          </dl>
        </div>
        <!-- <div class="org-info">
          <dl class="row">
            <dt class="col-9">Povprečni letni proračun v zadnjem letu</dt>
            <dd class="col-3">{{ formatEuro(organization.avg_revenue) }}</dd>
            <dt class="col-9">Število zaposlenih v zadnjem zaključenem letu</dt>
            <dd class="col-3">{{ organization.employed }}</dd>
            <dt class="col-9">
              Organizacija ima status humanitarne organizacije
            </dt>
            <dd class="col-3">{{ organization.is_charity ? 'DA' : 'NE' }}</dd>
            <dt class="col-9">
              Organizacija ima status delovanja v javnem interesu
            </dt>
            <dd class="col-3">
              {{ organization.has_public_interest ? 'DA' : 'NE' }}
            </dd>
            <dt class="col-9">
              Organizacija je vpisana v evidenco prostovoljskih organizacij
            </dt>
            <dd class="col-3">{{ organization.is_voluntary ? 'DA' : 'NE' }}</dd>
            <dt class="col-9">
              Organizacija je na seznamu upravičencev do 1 % dohodnine
            </dt>
            <dd class="col-3">{{ organization.zero5 ? 'DA' : 'NE' }}</dd>
            <dt class="col-9">
              Višina zbranih sredstev prek 1% dohodnine
            </dt>
            <dd class="col-3">{{ formatEuro(organization.zero5_amount) }}</dd>
          </dl>
        </div> -->
        <div class="org-review-date">
          Datum pregleda: {{ formatDate(organization.review_date) }}
        </div>
        <div class="org-donate">
          <donate-button
            text="Doniraj organizaciji"
            @click="toggleDonateModal"
          />
        </div>
      </div>
      <div class="col-12 col-md-7">
        <div class="org-criteria">
          <h4>Kriteriji</h4>
          <div class="row">
            <div
              v-for="(points, section) in groupedPointsDetails"
              :key="section"
              class="col-xl-4"
            >
              <h5 class="org-criteria-section-name">
                <nuxt-link
                  :to="{
                    name: 'metodologija',
                    hash: `#accordion-item-${sectionIndexFromName(section)}`,
                  }"
                >
                  <div>
                    <em>{{ splitNameAtColon(section)[0] }}</em>
                  </div>
                  <div>{{ splitNameAtColon(section)[1] }}</div>
                </nuxt-link>
              </h5>
              <div v-for="point in points" :key="point.name">
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    :id="`point-${point.name}`"
                    :checked="point.value"
                    disabled
                  />
                  <label class="form-check-label" :for="`point-${point.name}`">
                    <em>{{ splitNameAtColon(point.verbose_name)[0] }}: </em>
                    {{ splitNameAtColon(point.verbose_name)[1] }}
                  </label>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div class="text-right mt-4">
                <em>
                  Število izpolnjenih kriterijev {{ organization.points }}/{{
                    organization.points_details.length
                  }}
                </em>
              </div>
            </div>
          </div>
        </div>
        <div v-if="hasTaxDonationWidget" class="org-enprocent">
          <h4>Donacija prek 1% dohodnine</h4>
          <iframe
            id="enprocent_iframe"
            frameborder="0"
            width="800"
            height="600"
            style="max-width: 100%"
            :src="taxDonationWidgetUrl"
          ></iframe>
        </div>
      </div>
    </div>

    <transition name="fade-modal">
      <div
        v-if="showStarsModal"
        class="modal show"
        tabindex="-1"
        role="dialog"
        style="display: block"
      >
        <div
          class="modal-dialog modal-lg modal-dialog-centered"
          role="document"
        >
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Skupna ocena</h5>
              <div class="stars">
                <i
                  v-for="i in 5"
                  :key="i"
                  :class="[
                    'icon',
                    'icon-star',
                    { 'icon-star--full': organization.stars >= i },
                  ]"
                />
              </div>
              <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
                @click="toggleStarsModal(false)"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <p class="text-center">
                Skupna ocena organizacije je seštevek točk, ki jih organizacija
                prejme po posameznih kriterijih, ki so razvidni v spodnji
                tabeli. Več informacij o metodologiji lahko dobite
                <nuxt-link :to="{ name: 'metodologija' }">tukaj</nuxt-link>.
              </p>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <transition name="fade-modal">
      <div
        v-if="showDonateModal"
        class="modal show"
        tabindex="-1"
        role="dialog"
        style="display: block"
      >
        <div
          class="modal-dialog modal-lg modal-dialog-centered"
          role="document"
        >
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Doniraj organizaciji</h5>
              <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
                @click="toggleDonateModal(false)"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <div v-if="organization.account_number" class="qr-code-container">
                <amount-selector @change="onAmountChange" />
                <div ref="qrCode" class="qr-code"></div>
              </div>
              <p
                v-if="organization.donation_url || organization.account_number"
              >
                Organizaciji lahko doniraš tudi
                <template v-if="organization.donation_url">
                  na povezavi:
                  <a
                    :href="organization.donation_url"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="font-weight-normal"
                    style="word-break: break-all"
                    >{{ organization.donation_url }}</a
                  >
                  <template v-if="organization.account_number"> ali </template>
                </template>
                <template v-if="organization.account_number">
                  z nakazilom na TRR:
                  <span class="font-weight-normal">{{
                    organization.account_number
                  }}</span></template
                >.
              </p>
              <p v-else class="text-center">
                Podatkov kako lahko donirate organizaciji nimamo.
              </p>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade-backdrop">
      <div
        v-if="showStarsModal || showDonateModal"
        class="modal-backdrop show"
      />
    </transition>
  </div>
</template>

<script>
import _ from 'lodash';
import ContentTitle from '~/components/ContentTitle.vue';
import DonateButton from '~/components/Form/DonateButton.vue';
import AmountSelector from '~/components/AmountSelector.vue';
import formatPhoneNumberMixin from '~/mixins/formatPhoneNumber.js';

export default {
  components: {
    ContentTitle,
    DonateButton,
    AmountSelector,
  },
  mixins: [formatPhoneNumberMixin],
  // TODO: migrate?
  // validate({ params }) {
  //   return /^\d+$/.test(params.id);
  // },
  async setup() {
    const config = useRuntimeConfig();
    const route = useRoute();

    const orgId = route.params.id;
    const editKey = route.query.edit_key ? `?edit_key=${query.edit_key}` : '';

    const { data: organization } = await useAsyncData('organization', () => {
      const apiBase = process.server
        ? config.public.apiBaseServer
        : config.public.apiBase;
      return $fetch(`${apiBase}/api/organizations/${orgId}/${editKey}`);
    });

    return {
      apiBaseUrl: config.public.apiBase,
      organization,
    };
  },
  data() {
    return {
      showStarsModal: false,
      showDonateModal: false,
      qrCodeAbortController: null,
      hasTaxDonationWidget: false,
      taxDonationWidgetData: null,
    };
  },
  async mounted() {
    const res = await $fetch(
      `${this.apiBaseUrl}/api/organization-has-tax-donation/${this.organization.id}/`,
    );
    if (res.found) {
      this.enableTaxDonationWidget(res.ngo);
    }
  },
  beforeDestroy() {
    this.toggleStarsModal(false);
  },
  computed: {
    groupedPointsDetails() {
      return _.groupBy(this.organization.points_details, 'section');
    },
    taxDonationWidgetUrl() {
      const qs = new URLSearchParams({
        address: this.taxDonationWidgetData.address,
        city: this.taxDonationWidgetData.city,
        name: this.taxDonationWidgetData.name,
        percent: 1.0,
        postalCode: this.taxDonationWidgetData.postal_code,
        taxNumber: this.taxDonationWidgetData.tax_number,
      });
      return `https://www.cnvos.si/enprocent/embed/v2/?${qs.toString()}`;
    },
  },
  methods: {
    enableTaxDonationWidget(ngo) {
      this.taxDonationWidgetData = ngo;
      this.hasTaxDonationWidget = true;

      this.$nextTick(() => {
        if (typeof window !== 'undefined') {
          if (window.iFrameResize) {
            iFrameResize({ checkOrigin: false }, '#enprocent_iframe');
          } else {
            const script = document.createElement('script');
            script.onload = () => {
              iFrameResize({ checkOrigin: false }, '#enprocent_iframe');
            };
            script.src =
              'https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.2/iframeResizer.min.js';
            document.head.appendChild(script);
          }
        }
      });
    },
    sectionIndexFromName(section) {
      const sectionIndex = section.split(': ')[0].split(' ')[1];
      return Number(sectionIndex) + 1;
    },
    splitNameAtColon(section) {
      return section.split(': ');
    },
    toggleStarsModal(show = !this.showStarsModal) {
      if (typeof window !== 'undefined' && document.body.classList) {
        if (show) {
          document.body.classList.add('modal-open');
        } else {
          document.body.classList.remove('modal-open');
        }
      }
      this.showStarsModal = show;
    },
    toggleDonateModal(show = !this.showDonateModal) {
      if (typeof window !== 'undefined' && document.body.classList) {
        if (show) {
          document.body.classList.add('modal-open');
        } else {
          document.body.classList.remove('modal-open');
        }
      }
      this.showDonateModal = show;
    },
    getIconForUrl(url) {
      const domains = {
        facebook: ['facebook.com', 'fb.com', 'fb.me'],
        twitter: ['twitter.com'],
        instagram: ['instagram.com'],
        youtube: ['youtube.com', 'youtu.be'],
        vimeo: ['vimeo.com'],
      };

      return (
        _.keys(domains).find((key) =>
          domains[key].some((d) => url.includes(d)),
        ) || 'link'
      );
    },
    paragraphise(text) {
      const paragraphs = _.escape(text)
        .trim()
        .replace(/\r\n/g, '\n')
        .replace(/\r/g, '\n')
        .split(/\n\n+/g);
      return paragraphs
        .map((p) => `<p>${p.replace(/\n/g, '<br>')}</p>`)
        .join('');
    },
    formatEuro(value) {
      if (
        typeof Intl !== 'undefined' &&
        typeof Intl.NumberFormat !== 'undefined'
      ) {
        return new Intl.NumberFormat('sl-SI', {
          style: 'currency',
          currency: 'EUR',
        }).format(value);
      }
      return String(value);
    },
    formatDate(value) {
      if (
        typeof Intl !== 'undefined' &&
        typeof Intl.DateTimeFormat !== 'undefined'
      ) {
        return new Intl.DateTimeFormat('sl-SI').format(new Date(value));
      }
      return String(value);
    },
    async onAmountChange(newAmount) {
      if (this.qrCodeAbortController) {
        this.qrCodeAbortController.abort();
      }
      this.qrCodeAbortController = new AbortController();
      const { signal } = this.qrCodeAbortController;
      this.$refs.qrCode.textContent = 'Nalaganje QR kode...';

      const qrUrl = `${this.apiBaseUrl}/api/organizations-donation-qr-code/${this.organization.id}/?amount=${newAmount}`;
      try {
        const response = await fetch(qrUrl, { signal });
        const svgText = await response.text();
        this.$refs.qrCode.innerHTML = svgText;
      } catch (error) {
        if (error.name !== 'AbortError') {
          this.$refs.qrCode.innerHTML = '<strong>NAPAKA</strong>';
          console.error(error);
        }
      }
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

  .org-review-date {
    padding: 2rem 0;
    font-size: 1.25rem;
    font-weight: 300;
  }

  .org-donate {
    display: flex;
    justify-content: center;
    margin: 3rem 0;
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

    :deep(div) {
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

  .org-criteria {
    margin-bottom: 2rem;

    .org-criteria-section-name {
      margin-top: 1rem;
      margin-bottom: 1rem;
      border-top: 0.5rem solid $yellow;
      padding-top: 1rem;
      font-size: 16px;
      font-weight: 700;
      text-transform: uppercase;

      em {
        font-style: italic;
        font-weight: 400;
      }

      a {
        color: inherit;
      }
    }

    .form-check {
      margin-bottom: 0.5rem;
      padding-left: 2.75rem;
      min-height: 2.5rem;
    }

    .form-check-input {
      appearance: none;
      width: 2rem;
      height: 2rem;
      margin-top: 0;
      margin-left: -2.75rem;
      background-image: url('~/assets/svg/ne.svg');
      background-repeat: no-repeat;
      background-size: cover;

      &:checked {
        background-image: url('~/assets/svg/da.svg');
      }
    }

    .form-check-label {
      color: $body-color;
      line-height: 1.2;
      font-weight: 400;
    }

    .form-check-input:checked + .form-check-label {
      font-weight: 700;
    }
  }

  .org-enprocent {
    h4 {
      margin-bottom: 1rem;
    }

    iframe {
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
      font-size: 1.25rem;

      @include media-breakpoint-down(sm) {
        margin-top: 2rem;
        font-size: 1rem;
      }

      tr {
        border-top: 1px solid $blue;

        &:last-of-type {
          border-bottom: 1px solid $blue;
        }

        td {
          border: 0;
          padding-top: 1.25rem;
          padding-bottom: 1.25rem;

          @include media-breakpoint-down(sm) {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
          }

          &:first-of-type {
            padding-left: 0;
          }

          &:last-of-type {
            text-align: right;
            min-width: 4rem;
          }
        }
      }
    }

    .qr-code-container {
      margin-bottom: 2rem;

      .qr-code {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        width: 280px;
        height: 280px;
        background: #fff;
        border: 2px solid $blue;
        text-align: center;
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
