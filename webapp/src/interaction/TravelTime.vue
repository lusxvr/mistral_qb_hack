<script setup>
import {
    NumberField,
    NumberFieldContent,
    NumberFieldDecrement,
    NumberFieldIncrement,
    NumberFieldInput,
} from '@/components/ui/number-field'
import { useUserInfoStore } from '@/pinia/userInfo'

const store = useUserInfoStore()

const handleChange = (value) => {
    store.setMaxTravelTime(value)
}
</script>

<template>
    <NumberField 
        id="travel-time" 
        :default-value="3" 
        :min="1" 
        :max="14"
        @update:model-value="handleChange"
    >
        <div class="text-xs font-bold">Max. Travel Time in Hours</div>
        <NumberFieldContent>
            <NumberFieldDecrement />
            <NumberFieldInput />
            <NumberFieldIncrement />
        </NumberFieldContent>
    </NumberField>
</template>
