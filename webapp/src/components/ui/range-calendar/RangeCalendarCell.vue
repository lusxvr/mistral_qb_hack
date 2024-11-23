<script setup>
import { cn } from '@/lib/utils';
import { RangeCalendarCell, useForwardProps } from 'radix-vue';
import { computed } from 'vue';

const props = defineProps({
  date: { type: null, required: true },
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
  <RangeCalendarCell
    :class="
      cn(
        'relative p-0 text-center text-sm focus-within:relative focus-within:z-20 [&:has([data-selected])]:bg-slate-100 first:[&:has([data-selected])]:rounded-l-md last:[&:has([data-selected])]:rounded-r-md [&:has([data-selected][data-outside-view])]:bg-slate-100/50 [&:has([data-selected][data-selection-end])]:rounded-r-md [&:has([data-selected][data-selection-start])]:rounded-l-md dark:[&:has([data-selected])]:bg-slate-800 dark:[&:has([data-selected][data-outside-view])]:bg-slate-800/50',
        props.class,
      )
    "
    v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarCell>
</template>
