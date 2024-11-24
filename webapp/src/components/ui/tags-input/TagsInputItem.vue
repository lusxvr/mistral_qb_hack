<script setup>
import { cn } from '@/lib/utils';
import { TagsInputItem, useForwardProps } from 'radix-vue';

import { computed } from 'vue';

const props = defineProps({
  value: { type: [String, Object], required: true },
  disabled: { type: Boolean, required: false },
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
  <TagsInputItem
    v-bind="forwardedProps"
    :class="
      cn(
        'flex h-5 items-center rounded-md bg-slate-100 data-[state=active]:ring-slate-950 data-[state=active]:ring-2 data-[state=active]:ring-offset-2 ring-offset-white dark:bg-slate-800 dark:data-[state=active]:ring-slate-300 dark:ring-offset-slate-950',
        props.class,
      )
    "
  >
    <slot />
  </TagsInputItem>
</template>
