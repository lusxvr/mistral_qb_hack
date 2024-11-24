<script setup>
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { useCurrentRecommendationStore } from '@/pinia/currentRecommendation'
import { Plane, Bus, Train, Car, Timer, Calendar } from 'lucide-vue-next'

const recommendationStore = useCurrentRecommendationStore()
</script>

<template>
    <div class="w-full max-w-md mx-auto">
        <div class="bg-white rounded-lg shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl">
            <img 
                :src="recommendationStore.recommendation.imgAddress" 
                :alt="recommendationStore.recommendation.title" 
                width="600" 
                height="400" 
                class="w-full h-64 object-cover bg-gray-200" 
            />
            <div class="p-4 space-y-2">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-semibold">{{ recommendationStore.recommendation.title }}</h3>
                    <div class="text-gray-500">
                        {{ recommendationStore.recommendation.city }}, {{ recommendationStore.recommendation.country }}
                    </div>
                </div>
                <Badge>{{ recommendationStore.recommendation.amountPeople }} {{ recommendationStore.recommendation.amountPeople === 1 ? 'Person' : 'People' }}</Badge>
                <p class="text-gray-500">{{ recommendationStore.recommendation.description }}</p>
                <div class="w-full border-b"></div>
                <div class="flex items-center justify-between">
                    <div class="flex items-center gap-2">
                        <Plane v-if="recommendationStore.recommendation.travelMedium?.toLowerCase() === 'plane'" />
                        <Bus v-if="recommendationStore.recommendation.travelMedium?.toLowerCase() === 'bus'" />
                        <Train v-if="recommendationStore.recommendation.travelMedium?.toLowerCase() === 'train'" />
                        <Car v-if="recommendationStore.recommendation.travelMedium?.toLowerCase() === 'car'" />
                    </div>
                    <div class="flex items-center gap-2">
                        <Timer />
                        <div>{{ recommendationStore.recommendation.travelTime }}h</div>
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <Calendar />
                    <div class="text-sm text-gray-500">{{ recommendationStore.recommendation.amountNights }} {{ recommendationStore.recommendation.amountNights === 1 ? 'Night' : 'Nights' }}</div>
                </div>
                <div class="w-full border-b"></div>
                <div class="flex items-center justify-between">
                    <span class="text-lg font-bold">{{ recommendationStore.recommendation.price }}€</span>
                    <Button>Book Now</Button>
                </div>
            </div>
        </div>
    </div>
</template>