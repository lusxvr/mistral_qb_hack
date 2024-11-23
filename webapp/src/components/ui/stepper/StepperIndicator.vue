<script setup>
import { cn } from '@/lib/utils';
import { StepperIndicator, useForwardProps } from 'radix-vue';

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

const forwarded = useForwardProps(delegatedProps);
</script>

<template>
  <StepperIndicator
    v-bind="forwarded"
    :class="
      cn(
        'inline-flex items-center justify-center rounded-full text-slate-500/50 w-8 h-8 dark:text-slate-400/50',
        // Disabled
        'group-data-[disabled]:text-slate-500 group-data-[disabled]:opacity-50 dark:group-data-[disabled]:text-slate-400',
        // Active
        'group-data-[state=active]:bg-slate-900 group-data-[state=active]:text-slate-50 dark:group-data-[state=active]:bg-slate-50 dark:group-data-[state=active]:text-slate-900',
        // Completed
        'group-data-[state=completed]:bg-slate-100 group-data-[state=completed]:text-slate-900 dark:group-data-[state=completed]:bg-slate-800 dark:group-data-[state=completed]:text-slate-50',
        props.class,
      )
    "
  >
    <slot />
  </StepperIndicator>
</template>
