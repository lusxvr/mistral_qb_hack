<script setup>
import { cn } from '@/lib/utils';
import { Cross2Icon } from '@radix-icons/vue';
import { TagsInputItemDelete, useForwardProps } from 'radix-vue';
import { computed } from 'vue';

const props = defineProps({
  asChild: { type: Boolean, required: false },
  as: { type: null, required: false },
  class: { type: null, required: false },
});

const delegatedProps = computed(() => {
  const { class: _, ...delegated } = props;

  return delegated;
});

const forwardedProps = useForwardProps(delegatedProps);
</script>

<template>
  <TagsInputItemDelete
    v-bind="forwardedProps"
    :class="cn('flex rounded bg-transparent mr-1', props.class)"
  >
    <slot>
      <Cross2Icon class="w-4 h-4" />
    </slot>
  </TagsInputItemDelete>
</template>
