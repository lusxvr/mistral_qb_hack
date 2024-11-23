<script setup>
import { Slider } from '@/components/ui/slider'
import { ref } from 'vue'
const price = ref([400])
</script>

<template>
    <div class="flex flex-col items-start space-y-2">
        <div class="text-xs font-bold">Select Price</div>
        <Slider
            v-model="price"
            :default-value="[400]"
            :max="5000"
            :step="100"
        />
        <div class="flex flex-row justify-between w-full">
            <span class="text-xs">How much are you willing to spend?</span>
            <span class="text-xs"><{{ price[0] }}€</span>
        </div>
    </div>
</template>
