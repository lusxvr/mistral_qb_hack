<script setup>
import { ScrollArea } from '@/components/ui/scroll-area'
</script>

<template>
    <ScrollArea class="w-full h-[150px]">
        <div class="flex flex-col items-start w-full bg-slate-100 rounded-lg px-4 py-2">
            <div class="">User: I'd like to plan a vacation to Italy this summer.</div>
            <div class="">Agent: I'll help you plan your Italian vacation! Do you have specific regions in mind or would you like suggestions?</div>
            <div class="">User: I'm interested in visiting Rome and the Amalfi Coast.</div>
            <div class="">Agent: Great choices! Rome offers incredible history and culture, while the Amalfi Coast is perfect for scenic views and relaxation. How long are you planning to stay?</div>
            <div class="">User: I'm thinking about 10 days in total.</div>
            <div class="">Agent: That's a good duration. I'd suggest spending 4 days in Rome and 6 days along the Amalfi Coast. Would you like specific recommendations for each location?</div>
            <div class="">User: Yes, please! What are the must-see places in Rome?</div>
            <div class="">Agent: In Rome, you shouldn't miss the Colosseum, Vatican Museums, Roman Forum, and Trevi Fountain. Would you like a suggested daily itinerary?</div>
            <div class="">User: That would be very helpful, thanks!</div>
        </div>
    </ScrollArea>
</template>