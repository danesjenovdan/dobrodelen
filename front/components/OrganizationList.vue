<template>
  <div class="organization-list">
    <form action="#" method="get" @submit.prevent>
      <div class="form-row align-items-center justify-content-center">
        <div class="col-9 col-md-auto">
          <input class="form-control" type="text" placeholder="Poišči organizacijo" />
        </div>
        <div class="col-3 col-md-auto">
          <input class="form-control btn btn-warning" type="submit" value="Išči" />
        </div>
      </div>
    </form>
    <table class="table table-hover">
      <thead>
        <tr>
          <th class="can-sort desc">
            <span>Ime</span>
          </th>
          <th>
            <span>Opis</span>
          </th>
          <th class="can-sort">
            <span>Ocena</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="org in organizations" :key="org.id" @click="onOrgClick(org)">
          <td>
            <nuxt-link :to="{ name: 'org-id', params: { id: org.id } }" class="org-image-link">
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
            <nuxt-link :to="{ name: 'org-id', params: { id: org.id } }" class="org-title-link">
              <strong class="lead">{{ org.name }}</strong>
            </nuxt-link>
          </td>
          <td>
            <p class="lead">{{ org.description }}</p>
          </td>
          <td>
            <div class="stars">
              <i
                v-for="i in 5"
                :key="i"
                :class="['icon', 'icon-star', { 'icon-star--full': org.stars >= i }]"
              />
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    organizations: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      apiBaseUrl: process.env.API_BASE_URL,
    };
  },
  methods: {
    onOrgClick(org) {
      this.$router.push({ name: 'org-id', params: { id: org.id } });
    },
  },
};
</script>

<style lang="scss" scoped>
.organization-list {
  background: #f6f2f0;
  padding: 0 4em;

  @include media-breakpoint-down(sm) {
    padding: 0 1rem;
  }

  form {
    padding: 7rem 0;

    @include media-breakpoint-down(sm) {
      padding: 3rem 0;
    }

    .form-control {
      height: 61px;
      padding: 0 2rem;
      font-size: 1.5rem;
      border: 0;

      @include media-breakpoint-down(sm) {
        height: 3rem;
        padding: 0 1.25rem;
        font-size: 1rem;
      }

      &[type='text'] {
        width: 42rem;
        margin-right: 0.6rem;

        @include media-breakpoint-down(sm) {
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

        @include media-breakpoint-down(sm) {
          width: 100%;
        }
      }
    }
  }

  .table {
    @include media-breakpoint-down(sm) {
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

            .embed-responsive {
              width: 3rem;
              height: 3rem;
              margin: 0;
            }
          }

          .org-title-link {
            // display: inline-block;
            // margin-top: 2rem;
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

      @include media-breakpoint-down(sm) {
        font-size: 1rem;
      }

      &:first-child {
        width: 31rem;
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
          border-bottom-width: ($sort-arrow-diff - 1) * ($sort-arrow-size/$sort-arrow-diff);
          border-bottom-color: $body-color;
        }

        &::after {
          top: 53%;
          bottom: auto;

          border: $sort-arrow-size/2 solid transparent;
          border-bottom-width: 1 * ($sort-arrow-size/$sort-arrow-diff);
          border-top-width: ($sort-arrow-diff - 1) * ($sort-arrow-size/$sort-arrow-diff);
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

      .lead {
        line-height: 1.4;
      }

      strong.lead {
        font-weight: 600;
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
