<template>
  <vue-pell-editor
    :value="value"
    :actions="editorOptions"
    default-paragraph-separator="p"
    @change="onEditorChange($event, 'note')"
  />
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      editorOptions: ['bold', 'italic', 'olist', 'ulist'],
    };
  },
  methods: {
    onEditorChange({ editor }, key) {
      const content = editor.querySelector('.pell-content');

      /*
       * Fix all illegal variations of nested paragraphs and lists,
       * and move them out of each other
       */
      // let nested;
      // eslint-disable-next-line no-cond-assign
      // while (
      //   (nested = content.querySelector('p > p, p > ul, ul > p')) != null
      // ) {
      //   content.insertBefore(nested, nested.parentElement);
      // }

      /*
       * Remove paragraph and div elements inside of list elements
       */
      // eslint-disable-next-line no-cond-assign
      // while ((nested = content.querySelector('li p, li div')) != null) {
      //   nested.outerHTML = nested.innerHTML;
      // }

      /*
       * Remove all span elements since they are only used for styling and we
       * remove styles
       */
      // eslint-disable-next-line no-cond-assign
      // while ((nested = content.querySelector('span')) != null) {
      //   nested.outerHTML = nested.innerHTML;
      // }

      /*
       * If there is a top level br element wrap it in a paragraph
       */
      // let children = content.childNodes;
      // for (let i = 0; i < children.length; i += 1) {
      //   const child = children[i];
      //   if (child.nodeType === 3 || child.tagName === 'BR') {
      //     const p = document.createElement('p');
      //     content.insertBefore(p, child);
      //     p.appendChild(child);
      //   }
      // }

      /*
       * If there are empty top level elements remove them
       */
      // children = content.childNodes;
      // for (let i = 0; i < children.length; i += 1) {
      //   const child = children[i];
      //   if (!child.innerHTML || !child.innerHTML.trim()) {
      //     content.removeChild(child);
      //   }
      // }

      /*
       * Remove all style and dir attributes on all elements
       */
      const all = content.querySelectorAll('*');
      for (let i = 0; i < all.length; i += 1) {
        const el = all[i];
        el.removeAttribute('style');
        el.removeAttribute('dir');
        el.removeAttribute('class');
      }

      this.$emit('input', content.innerHTML);
    },
  },
};
</script>

<style lang="scss" scoped>
.vp-editor {
  /deep/ .vp-editor__placeholder {
    display: none;
  }

  /deep/ .pell-content {
    height: 500px;
    background: rgba(#f6f2f0, 0.4);
    border-bottom: 2px solid rgba($blue, 0.3);
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;

    font-size: 1.5rem;

    &,
    &:focus {
      outline: 0;
      box-shadow: none;
    }

    &:focus {
      border-bottom-color: $blue;
    }
  }

  &.is-invalid {
    /deep/ .pell-content {
      color: $red;
      border-bottom-color: rgba($red, 0.3);

      &:focus {
        border-bottom-color: $red;
      }
    }
  }
}
</style>
