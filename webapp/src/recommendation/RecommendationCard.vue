<script setup>
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { ScrollArea } from '@/components/ui/scroll-area'
import { useCurrentRecommendationStore } from '@/pinia/currentRecommendation'
import { Plane, Bus, Train, Car, Timer, Calendar } from 'lucide-vue-next'
import { computed } from 'vue'

const recommendationStore = useCurrentRecommendationStore()

const formatPrice = (price) => {
    if (!price || price.toString().toLowerCase() === 'nan') {
        return '-'
    }
    return `${price}€`
}

// Computed property für die Transportmittel
const travelMediums = computed(() => {
    if (!recommendationStore.recommendation.travelMedium) return []
    return recommendationStore.recommendation.travelMedium
        .toLowerCase()
        .split(',')
        .map(medium => medium.trim())
})
</script>

<template>
    <ScrollArea class="h-full">
        <div class="w-full max-w-md mx-auto mb-8">
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
                            <Plane v-if="travelMediums.includes('plane')" />
                            <Bus v-if="travelMediums.includes('bus')" />
                            <Train v-if="travelMediums.includes('train')" />
                            <Car v-if="travelMediums.includes('car')" />
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
                        <span class="text-lg font-bold">{{ formatPrice(recommendationStore.recommendation.price) }}</span>
                        <Button>Book Now</Button>
                    </div>
                </div>
            </div>
        </div>
        <div class="w-full max-w-md mx-auto h-16">
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl">
                <div class="flex h-full">
                    <div class="w-1/2 h-full">
                        <img 
                            :src="recommendationStore.adAuction.imageLink" 
                            :alt="recommendationStore.adAuction.productName" 
                            class="w-full h-full object-cover"
                        />
                    </div>
                    <div class="w-1/2 p-4 flex flex-col justify-between h-full">
                        <h3 class="text-lg font-semibold text-left">{{ recommendationStore.adAuction.productName }}</h3>
                        <div class="flex justify-end">
                            <Button variant="outline" size="sm">
                                {{ formatPrice(recommendationStore.adAuction.price) }}
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </ScrollArea>
</template>