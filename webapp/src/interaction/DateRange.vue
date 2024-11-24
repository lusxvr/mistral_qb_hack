<script setup>
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import { RangeCalendar } from '@/components/ui/range-calendar'
import { getLocalTimeZone, today } from '@internationalized/date'
import { ref, onMounted } from 'vue'
import { Button } from '@/components/ui/button'
import { useUserInfoStore } from '@/pinia/userInfo'

const store = useUserInfoStore()

const handleDateChange = (range) => {
  if (!range || !range.start || !range.end) {
    // invalid range
    return
  }

  const dateUpdate = {
    start: range.start.toDate('UTC').toISOString(),
    end: range.end.toDate('UTC').toISOString()
  }
  
  store.setDate(dateUpdate)
}

// Initialer Wert
const value = ref({
  start: today(getLocalTimeZone()),
  end: today(getLocalTimeZone()).add({ days: 7 })
})
</script>

<template>
  <div class="flex flex-col items-start space-y-1">
    <div class="text-xs font-bold">Select dates</div>
    <Popover>
      <PopoverTrigger as-child>
        <Button variant="outline">Date Range</Button>
      </PopoverTrigger>
      <PopoverContent>
        <RangeCalendar 
          v-model="value" 
          @update:model-value="handleDateChange"
        />
      </PopoverContent>
    </Popover>
  </div>
</template>
