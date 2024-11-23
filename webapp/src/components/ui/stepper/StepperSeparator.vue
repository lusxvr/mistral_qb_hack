<script setup>
import { cn } from '@/lib/utils';
import { StepperSeparator, useForwardProps } from 'radix-vue';

import { computed } from 'vue';

const props = defineProps({
  orientation: { type: String, required: false },
  decorative: { type: Boolean, required: false },
  asChild: { type: Boolean, required: false },
  as: { type: null, required: false },
  class: { type: null, required: false },
});

const delegatedProps = computed(() => {
  const { class: _, ...delegated } = props;

  return delegated;
});

const forwarded = useForwardProps(delegatedProps);
</script>

<template>
  <StepperSeparator
    v-bind="forwarded"
    :class="
      cn(
        'bg-slate-100 dark:bg-slate-800',
        // Disabled
        'group-data-[disabled]:bg-slate-100 group-data-[disabled]:opacity-50 dark:group-data-[disabled]:bg-slate-800',
        // Completed
        'group-data-[state=completed]:bg-slate-900 dark:group-data-[state=completed]:bg-slate-50',
        props.class,
      )
    "
  />
</template>
