<script setup>
import { Button } from '@/components/ui/button'
import { TagsInput, TagsInputInput, TagsInputItem, TagsInputItemDelete, TagsInputItemText } from '@/components/ui/tags-input'
import DateRange from '@/interaction/DateRange.vue'
import Price from '@/interaction/Price.vue'
import Vibe from '@/interaction/Vibe.vue'
import TravelMedium from '@/interaction/TravelMedium.vue'
import TravelTime from '@/interaction/TravelTime.vue'
import AmountPeople from '@/interaction/AmountPeople.vue'
import { useUserInfoStore } from '@/pinia/userInfo'
import { ref, computed } from 'vue'

const userInfoStore = useUserInfoStore()
const open = ref(false)

// Helper function to format the date
const formatDate = (dateString) => {
    if (!dateString) return ''
    const date = new Date(dateString)
    return date.toLocaleDateString('de-DE', {
        day: '2-digit',
        month: '2-digit',
        year: '2-digit'
    })
}

// Computed property for the active filters with type information
const activeFilters = computed(() => {
    const filters = []
    const filter = userInfoStore.filter

    // Date
    if (filter.date.start && filter.date.end) {
        filters.push({
            type: 'date',
            value: `${formatDate(filter.date.start)} - ${formatDate(filter.date.end)}`
        })
    }

    // Price
    if (filter.maxPrice) {
        filters.push({
            type: 'price',
            value: `Max ${filter.maxPrice}€`
        })
    }

    // Vibe (Array)
    if (filter.vibe && filter.vibe.length > 0) {
        filter.vibe.forEach(v => {
            filters.push({
                type: 'vibe',
                value: v,
                originalValue: v
            })
        })
    }

    // Travel medium
    if (filter.travelMedium) {
        filters.push({
            type: 'travelMedium',
            value: filter.travelMedium
        })
    }

    // Travel time
    if (filter.maxTravelTime) {
        filters.push({
            type: 'travelTime',
            value: `${filter.maxTravelTime}h max`
        })
    }

    // Person amount
    if (filter.personAmount) {
        filters.push({
            type: 'personAmount',
            value: `${filter.personAmount} ${filter.personAmount === 1 ? 'Person' : 'People'}`
        })
    }

    return filters
})

// handle delete
const handleDelete = (filter) => {
    switch (filter.type) {
        case 'date':
            userInfoStore.setDate({ start: null, end: null })
            break
        case 'price':
            userInfoStore.setMaxPrice(null)
            break
        case 'vibe':
            const newVibe = userInfoStore.filter.vibe.filter(v => v !== filter.originalValue)
            userInfoStore.setVibe(newVibe)
            break
        case 'travelMedium':
            userInfoStore.setTravelMedium(null)
            break
        case 'travelTime':
            userInfoStore.setMaxTravelTime(null)
            break
        case 'personAmount':
            userInfoStore.setPersonAmount(null)
            break
    }
}
</script>

<template>
    <div v-if="open"
        class="w-full flex flex-col space-y-4 mb-4 items-start transform transition-all duration-300 ease-out border p-4 rounded-lg"
        :class="open ? 'translate-y-0 opacity-100' : '-translate-y-4 opacity-0'">
        <DateRange />
        <Price class="w-[24rem]" />
        <Vibe />
        <TravelMedium />
        <TravelTime />
        <AmountPeople />
    </div>
    <div class="w-full flex space-x-2">
        <Button @click="open = !open" :variant="open ? 'default' : 'outline'">
            <span v-if="!open">Configure</span>
            <span v-else>Close</span>
        </Button>
        <div>
            <TagsInput class="border-none">
                <TagsInputItem v-for="filter in activeFilters" :key="filter.value" :value="filter.value">
                    <TagsInputItemText>{{ filter.value }}</TagsInputItemText>
                    <TagsInputItemDelete @click="handleDelete(filter)" />
                </TagsInputItem>
            </TagsInput>
        </div>
    </div>
</template>