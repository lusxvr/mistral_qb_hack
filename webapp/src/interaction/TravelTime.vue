<script setup>
import { Label } from '@/components/ui/label'
import {
    NumberField,
    NumberFieldContent,
    NumberFieldDecrement,
    NumberFieldIncrement,
    NumberFieldInput,
} from '@/components/ui/number-field'
</script>

<template>
    <NumberField id="travel-time" :default-value="2" :min="1" :max="14">
        <div class="text-xs font-bold">Max. Travel Time in Hours</div>
        <NumberFieldContent>
            <NumberFieldDecrement />
            <NumberFieldInput />
            <NumberFieldIncrement />
        </NumberFieldContent>
    </NumberField>
</template>
