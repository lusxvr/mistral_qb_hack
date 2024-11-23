<script setup>
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import { RangeCalendar } from '@/components/ui/range-calendar'
import { getLocalTimeZone, today } from '@internationalized/date'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'

const start = today(getLocalTimeZone())
const end = start.add({ days: 7 })

const value = ref({
  start,
  end,
})
</script>

<template>
  <div class="flex flex-col items-start space-y-1">
    <div class="text-xs font-bold">Select dates</div>
    <Popover>
      <PopoverTrigger as-child>
      <Button variant="outline" class="">Date Range</Button>
    </PopoverTrigger>
    <PopoverContent>
      <RangeCalendar v-model="value" class="" />
      </PopoverContent>
    </Popover>
  </div>
</template>
