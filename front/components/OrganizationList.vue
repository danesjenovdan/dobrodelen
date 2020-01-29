<template>
  <div class="organization-list">
    <form action="#" method="get" @submit.prevent>
      <div class="form-row align-items-center justify-content-center">
        <div class="col-12 col-md-6 col-md-auto">
          <input
            v-model="searchText"
            class="form-control"
            type="text"
            placeholder="Poišči organizacijo"
          />
        </div>
        <!-- <div class="col-3 col-md-auto">
          <input class="form-control btn btn-warning" type="submit" value="Išči" />
        </div> -->
      </div>
      <div class="form-row align-items-center justify-content-center">
        <div class="col-12 col-md-6 col-md-auto text-right">
          <button
            type="button"
            class="btn btn-sm btn-link"
            @click="showAdvanced = !showAdvanced"
          >
            Napredno iskanje
          </button>
        </div>
      </div>
      <div
        v-if="showAdvanced"
        class="form-row align-items-center justify-content-center"
      >
        <div class="col-12 col-md-10 col-md-auto">
          <form-category title="Področja delovanja">
            <div class="row">
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="1"
                  label="Človekove pravice, demokracija in enakost"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="2"
                  label="Izobraževanje, raziskave in razvoj"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="3"
                  label="Kultura"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="4"
                  label="Mladina, otroci"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="5"
                  label="Razvojno sodelovanje"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="6"
                  label="Sociala"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="7"
                  label="Šport"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="8"
                  label="Okolje, narava in prostor"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="9"
                  label="Zdravje"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="11"
                  label="Starejši"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.area"
                  type="checkbox"
                  name="area"
                  :value="10"
                  label="Drugo"
                />
              </div>
            </div>
          </form-category>

          <form-category title="Statusi">
            <div class="row">
              <div class="col-md-6">
                <selection-option
                  v-model="filters.is_charity"
                  type="checkbox"
                  name="is_charity"
                  label="Organizacija ima status humanitarne organizacije"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.has_public_interest"
                  type="checkbox"
                  name="has_public_interest"
                  label="Organizacija ima status delovanja v javnem interesu"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.is_voluntary"
                  type="checkbox"
                  name="is_voluntary"
                  label="Organizacija je vpisana v evidenco prostovoljskih organizacij"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.zero5"
                  type="checkbox"
                  name="zero5"
                  label="Organizacija je na seznamu upravičencev do 0,5 % dohodnine"
                />
              </div>
            </div>
          </form-category>

          <div class="row">
            <div class="col-md-6">
              <form-category title="Število zaposlenih">
                <select v-model="filters.employed" class="custom-select">
                  <option
                    v-for="employed in employmentFilters"
                    :key="employed.label"
                    :value="employed.label"
                  >
                    {{ employed.label }}
                  </option>
                </select>
              </form-category>
            </div>
            <div class="col-md-6">
              <form-category title="Proračun">
                <select v-model="filters.budget" class="custom-select">
                  <option
                    v-for="budget in budgetFilters"
                    :key="budget.label"
                    :value="budget.label"
                  >
                    {{ budget.label }}
                  </option>
                </select>
              </form-category>
            </div>
          </div>

          <form-category title="Regije">
            <div class="row">
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="1"
                  label="Gorenjska"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="2"
                  label="Goriška"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="3"
                  label="Jugovzhodna Slovenija"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="4"
                  label="Koroška"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="5"
                  label="Notranjskokraška"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="6"
                  label="Obalnokraška"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="7"
                  label="Osrednjeslovenska"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="8"
                  label="Podravska"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="9"
                  label="Pomurska"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="10"
                  label="Posavska"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="11"
                  label="Savinjska"
                />
              </div>
              <div class="col-md-6">
                <selection-option
                  v-model="filters.region"
                  type="checkbox"
                  name="region"
                  :value="12"
                  label="Zasavska"
                />
              </div>
            </div>
          </form-category>
        </div>
      </div>
    </form>
    <table class="table table-hover">
      <thead>
        <tr>
          <th
            :class="[
              'can-sort',
              { desc: sortKey === 'name' && !sortAsc },
              { asc: sortKey === 'name' && sortAsc },
            ]"
            @click="changeSort('name')"
          >
            <span>Ime</span>
          </th>
          <th>
            <span>Opis</span>
          </th>
          <th
            :class="[
              'can-sort',
              { desc: sortKey === 'stars' && !sortAsc },
              { asc: sortKey === 'stars' && sortAsc },
            ]"
            @click="changeSort('stars')"
          >
            <span>Ocena</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="org in sortedOrgs" :key="org.id" @click="onOrgClick(org)">
          <td>
            <nuxt-link
              :to="{ name: 'organizacija-id', params: { id: org.id } }"
              class="org-image-link"
            >
              <div class="embed-responsive embed-responsive-1by1">
                <div class="embed-responsive-item">
                  <div class="img-container">
                    <img
                      :src="
                        org.cover_photo
                          ? `${apiBaseUrl}${org.cover_photo.url}`
                          : '/img/placeholder.png'
                      "
                      alt="organization image"
                      class="rounded-circle bg-dark"
                    />
                  </div>
                </div>
              </div>
            </nuxt-link>
            <nuxt-link
              :to="{ name: 'organizacija-id', params: { id: org.id } }"
              class="org-title-link"
            >
              <strong class="lead">{{ org.name }}</strong>
            </nuxt-link>
          </td>
          <td>
            <p class="lead clamp-lines">{{ shorten(org.description) }}</p>
          </td>
          <td>
            <div class="stars">
              <i
                v-for="i in 5"
                :key="i"
                :class="[
                  'icon',
                  'icon-star',
                  { 'icon-star--full': org.stars >= i },
                ]"
              />
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { debounce } from 'lodash';
import stableSort from 'stable';
import FormCategory from '~/components/Form/FormCategory.vue';
import SelectionOption from '~/components/Form/SelectionOption.vue';

export default {
  components: {
    FormCategory,
    SelectionOption,
  },
  props: {
    organizations: {
      type: Array,
      required: true,
    },
    sortQuery: {
      type: String,
      default: '-stars',
    },
    searchQuery: {
      type: String,
      default: '',
    },
  },
  data() {
    const [sortKey, sortAsc] =
      this.sortQuery[0] === '-'
        ? [this.sortQuery.slice(1), false]
        : [this.sortQuery, true];

    const initialFilters = {
      area: [],
      region: [],
      is_charity: false,
      has_public_interest: false,
      is_voluntary: false,
      zero5: false,
      employed: 'Vsi',
      budget: 'Vsi',
    };

    const employmentFilters = [
      { label: 'Vsi', fn: (o) => true },
      { label: '0', fn: (o) => o.employed === 0 },
      { label: '1 – 5', fn: (o) => o.employed >= 1 && o.employed <= 5 },
      { label: '6 – 10', fn: (o) => o.employed >= 6 && o.employed <= 10 },
      { label: '11 – 50', fn: (o) => o.employed >= 11 && o.employed <= 50 },
      { label: 'Več kot 50', fn: (o) => o.employed > 50 },
    ];

    const budgetFilters = [
      {
        label: 'Vsi',
        fn: (o) => true,
      },
      {
        label: '0 – 10.000 €',
        fn: (o) => o.avg_revenue >= 0 && o.avg_revenue <= 10000,
      },
      {
        label: '10.001 – 50.000 €',
        fn: (o) => o.avg_revenue > 10000 && o.avg_revenue <= 50000,
      },
      {
        label: '50.001 – 250.000 €',
        fn: (o) => o.avg_revenue > 50000 && o.avg_revenue <= 250000,
      },
      {
        label: '250.001 – 1.000.000 €',
        fn: (o) => o.avg_revenue > 250000 && o.avg_revenue <= 1000000,
      },
      {
        label: 'Več kot 1.000.000 €',
        fn: (o) => o.avg_revenue > 1000000,
      },
    ];

    return {
      apiBaseUrl: process.env.API_BASE_URL,
      sortKey,
      sortAsc,
      searchText: this.searchQuery,
      showAdvanced: false,
      filters: initialFilters,
      employmentFilters,
      budgetFilters,
    };
  },
  computed: {
    selectedEmploymentFilter() {
      const filter = this.employmentFilters.find(
        (f) => f.label === this.filters.employed,
      );
      return filter || { label: '', fn: (o) => true };
    },
    selectedBudgetFilter() {
      const filter = this.budgetFilters.find(
        (f) => f.label === this.filters.budget,
      );
      return filter || { label: '', fn: (o) => true };
    },
    filteredOrgs() {
      let orgs = this.organizations || [];

      const textFilters = this.searchText
        .toLowerCase()
        .split(/\s+/g)
        .map((s) => s.trim())
        .filter(Boolean);

      if (textFilters && textFilters.length) {
        orgs = orgs.filter((org) => {
          const allNames = `${org.name} ${org.additional_names}`;
          return textFilters.every((textFilter) => {
            return allNames.toLowerCase().includes(textFilter);
          });
        });
      }

      if (this.filters.area.length) {
        orgs = orgs.filter((org) => {
          return this.filters.area.some((a) => {
            return org.area.includes(a);
          });
        });
      }
      if (this.filters.region.length) {
        orgs = orgs.filter((org) => {
          return this.filters.region.some((r) => {
            return org.region.includes(r);
          });
        });
      }

      if (this.filters.is_charity) {
        orgs = orgs.filter((org) => {
          return org.is_charity;
        });
      }
      if (this.filters.has_public_interest) {
        orgs = orgs.filter((org) => {
          return org.has_public_interest;
        });
      }
      if (this.filters.is_voluntary) {
        orgs = orgs.filter((org) => {
          return org.is_voluntary;
        });
      }
      if (this.filters.zero5) {
        orgs = orgs.filter((org) => {
          return org.zero5;
        });
      }

      orgs = orgs.filter(this.selectedEmploymentFilter.fn);
      orgs = orgs.filter(this.selectedBudgetFilter.fn);

      return orgs;
    },
    sortedOrgs() {
      return stableSort(this.filteredOrgs, (a, b) => {
        if (!this.sortAsc) {
          [a, b] = [b, a];
        }

        const aVal = a[this.sortKey];
        const bVal = b[this.sortKey];
        if (aVal === bVal) {
          return 0;
        }

        const aType = typeof aVal;
        const bType = typeof bVal;
        if (aType === bType) {
          if (aType === 'number') {
            return aVal - bVal;
          }
          if (aType === 'string') {
            return aVal.localeCompare(bVal, 'sl');
          }
        }
        return String(aVal).localeCompare(String(bVal), 'sl');
      });
    },
  },
  watch: {
    searchText() {
      this.emitChange();
    },
  },
  methods: {
    changeSort(key) {
      if (key === this.sortKey) {
        this.sortAsc = !this.sortAsc;
      } else {
        this.sortAsc = true;
        this.sortKey = key;
      }
      this.emitChange();
    },
    emitChange: debounce(function emitChange() {
      this.$emit('change', {
        sort: `${this.sortAsc ? '' : '-'}${this.sortKey}`,
        search: this.searchText,
      });
    }, 250),
    onOrgClick(org) {
      this.$router.push({ name: 'organizacija-id', params: { id: org.id } });
    },
    shorten(text, max = 320) {
      if (text.length > max) {
        return `${text.slice(0, text.lastIndexOf(' ', max))} ...`;
      }
      return text;
    },
  },
};
</script>

<style lang="scss" scoped>
.organization-list {
  background: #f6f2f0;
  padding: 0 4rem 4rem;
  margin-bottom: 3.5rem;

  @include media-breakpoint-down(md) {
    padding: 0 1rem 1rem;
    margin-bottom: 1rem;
  }

  form {
    padding: 7rem 0;

    @include media-breakpoint-down(md) {
      padding: 3rem 0;
    }

    fieldset /deep/ {
      margin-top: 1rem;

      legend {
        font-size: 1.25rem;
        margin-bottom: 0;
      }

      .custom-control:last-of-type {
        margin-bottom: 0;
      }

      .custom-control-label {
        font-size: 1rem;
        margin: 0.25rem 0;
      }

      .custom-select {
        border: none;
        margin: 0.25rem 0;
      }
    }

    .form-control {
      height: 61px;
      padding: 0 2rem;
      font-size: 1.5rem;
      border: 0;

      @include media-breakpoint-down(md) {
        height: 3rem;
        padding: 0 1.25rem;
        font-size: 1rem;
      }

      &[type='text'] {
        // width: 42rem;
        margin-right: 0.6rem;

        @include media-breakpoint-down(md) {
          width: 100%;
        }

        &::placeholder {
          letter-spacing: 0.2em;
        }
      }

      &[type='submit'] {
        width: 12rem;
        font-weight: 600;
        letter-spacing: 0.2em;

        @include media-breakpoint-down(md) {
          width: 100%;
        }
      }
    }
  }

  .table {
    margin-bottom: 0;

    @include media-breakpoint-down(md) {
      &,
      thead,
      tbody {
        display: block;
      }

      tr {
        display: flex;
        flex-direction: column-reverse;
      }

      thead tr {
        flex-direction: row;
      }

      th:nth-child(2),
      td:nth-child(2) {
        display: none;
      }

      tbody {
        tr {
          position: relative;

          td:nth-child(1) {
            padding: 0 1rem 1rem;
          }

          .org-image-link {
            // display: none;
            position: absolute;
            top: 1rem;
            left: 1rem;

            .embed-responsive {
              width: 3rem;
              height: 3rem;
              margin: 0;
            }
          }

          strong.lead {
            display: block;
            // text-align: center;
            font-size: 1.15rem;
          }

          td:nth-child(3) {
            padding: 1rem 1rem 0.5rem;
            border-bottom: 0;

            .stars {
              text-align: right;
              // position: absolute;
              bottom: 0.5rem;
              right: 0.5rem;
              height: 3rem;
              display: flex;
              justify-content: flex-end;
              align-items: center;

              .icon {
                width: 2rem;
                height: 2rem;
              }
            }
          }
        }
      }
    }

    th,
    td {
      padding-left: 1rem;
      padding-right: 1rem;
      border-top: 0;
    }

    th {
      font-size: 1.1rem;
      font-weight: 600;
      letter-spacing: 0.2em;
      position: relative;
      cursor: default;
      border-top: 0;
      border-bottom: 1px solid $blue;

      @include media-breakpoint-down(md) {
        font-size: 1rem;
      }

      &:first-child {
        width: 31rem;

        @include media-breakpoint-down(xl) {
          width: 20rem;
        }

        @include media-breakpoint-down(md) {
          width: 95%;
        }
      }

      &:last-child {
        width: 17rem;
      }

      &.can-sort {
        padding-left: 2.5rem;
        cursor: pointer;

        $sort-arrow-size: 0.9rem;
        $sort-arrow-diff: 3;

        &::before,
        &::after {
          content: '';
          display: block;
          position: absolute;
          left: 0.95rem;
          bottom: 53%;
          width: $sort-arrow-size;
          height: $sort-arrow-size;
          cursor: pointer;

          border: $sort-arrow-size/2 solid transparent;
          border-top-width: 1 * ($sort-arrow-size/$sort-arrow-diff);
          border-bottom-width: ($sort-arrow-diff - 1) *
            ($sort-arrow-size/$sort-arrow-diff);
          border-bottom-color: $body-color;
        }

        &::after {
          top: 53%;
          bottom: auto;

          border: $sort-arrow-size/2 solid transparent;
          border-bottom-width: 1 * ($sort-arrow-size/$sort-arrow-diff);
          border-top-width: ($sort-arrow-diff - 1) *
            ($sort-arrow-size/$sort-arrow-diff);
          border-top-color: $body-color;
        }

        &.asc::before {
          border-bottom-color: $blue;
        }

        &.desc::after {
          border-top-color: $blue;
        }
      }
    }

    td {
      padding-top: 1.25rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid $blue;

      a {
        color: inherit;
      }

      .embed-responsive {
        max-width: 4rem;
        height: 4rem; // Chrome bug fix
        float: left;
        margin-top: 0.25rem;
        margin-right: 2rem;

        .img-container {
          width: 100%;
          height: 100%;

          img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: contain;
            object-position: center;
          }
        }
      }

      .org-title-link {
        float: left;
        width: calc(100% - 6rem);

        @include media-breakpoint-down(md) {
          width: 100%;
        }
      }

      .lead {
        line-height: 1.4;
      }

      strong.lead {
        font-weight: 600;
      }

      .clamp-lines {
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }

      .stars {
        .icon {
          margin: 0 0.2rem;
        }
      }
    }

    tbody tr {
      cursor: pointer;
    }
  }
}
</style>
