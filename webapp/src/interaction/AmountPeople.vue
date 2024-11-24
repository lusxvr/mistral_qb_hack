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
    store.setPersonAmount(value)
}
</script>

<template>
    <NumberField 
        id="amount-people" 
        :default-value="1" 
        :min="1" 
        :max="6"
        @update:model-value="handleChange"
    >
        <div class="text-xs font-bold">Amount of People</div>
        <NumberFieldContent>
            <NumberFieldDecrement />
            <NumberFieldInput />
            <NumberFieldIncrement />
        </NumberFieldContent>
    </NumberField>
</template>
