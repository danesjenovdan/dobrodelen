<template>
  <div class="organization-list">
    <form action="#" method="get" @submit.prevent>
      <div class="form-row align-items-center justify-content-center">
        <div class="col-auto">
          <input class="form-control" type="text" placeholder="Poišči organizacijo" />
        </div>
        <div class="col-auto">
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
            <nuxt-link :to="{ name: 'org-id', params: { id: org.id } }">
              <div class="embed-responsive embed-responsive-1by1">
                <div class="embed-responsive-item">
                  <div class="img-container">
                    <img
                      :src="
                        org.cover_photo
                          ? `${process.env.API_BASE_URL}${org.cover_photo.url}`
                          : '/img/placeholder.png'
                      "
                      alt="organization image"
                      class="rounded-circle bg-dark"
                    />
                  </div>
                </div>
              </div>
            </nuxt-link>
            <nuxt-link :to="{ name: 'org-id', params: { id: org.id } }">
              <strong class="lead">{{ org.name }}</strong>
            </nuxt-link>
          </td>
          <td>
            <p class="lead">{{ org.description }}</p>
          </td>
          <td>
            <i
              v-for="i in 5"
              :key="i"
              :class="['icon', 'icon-star', { 'icon-star--full': org.stars >= i }]"
            />
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

  form {
    padding: 7rem 0;

    .form-control {
      height: 61px;
      padding: 0 2rem;
      font-size: 1.5rem;

      border: 0;

      &[type='text'] {
        width: 42rem;
        margin-right: 0.6rem;

        &::placeholder {
          letter-spacing: 0.2em;
        }
      }

      &[type='submit'] {
        width: 12rem;
        font-weight: 600;
        letter-spacing: 0.2em;
      }
    }
  }

  .table {
    th,
    td {
      padding-left: 1rem;
      padding-right: 1rem;
    }

    th {
      font-size: 1.1rem;
      font-weight: 600;
      letter-spacing: 0.2em;
      position: relative;
      cursor: default;
      border-top: 0;
      border-bottom: 1px solid $blue;

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

      .icon {
        margin: 0 0.2rem;
      }
    }

    tbody tr {
      cursor: pointer;
    }
  }
}
</style>
