<script setup>
import { Slider } from '@/components/ui/slider'
import { useUserInfoStore } from '@/pinia/userInfo'
import { computed } from 'vue'

const store = useUserInfoStore()

const sliderValue = computed({
  get: () => [store.filter.maxPrice],
  set: ([value]) => store.setMaxPrice(value)
})
</script>

<template>
    <div class="flex flex-col items-start space-y-2">
        <div class="text-xs font-bold">Select Price</div>
        <Slider
            v-model="sliderValue"
            :default-value="[400]"
            :max="5000"
            :step="100"
        />
        <div class="flex flex-row justify-between w-full">
            <span class="text-xs">How much are you willing to spend?</span>
            <span class="text-xs">{{ store.filter.maxPrice }}€</span>
        </div>
    </div>
</template>
