<script setup>
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'

import { Plane, Bus, Timer, Calendar } from 'lucide-vue-next';
</script>

<template>
    <div class="w-full max-w-md mx-auto">
        <div
            class="bg-white rounded-lg shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl">
            <img src="" alt="Product Image" width={600} height={400} class="w-full h-64 object-cover bg-gray-200" />
            <div class="p-4 space-y-2">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-semibold">Title</h3>
                    <div class="text-gray-500">City, Country</div>
                </div>
                <Badge>2 Persons</Badge>
                <p class="text-gray-500">This is a description of the product.</p>
                <div class="w-full border-b"></div>
                <div class="flex items-center justify-between">
                    <div class="flex items-center gap-2">
                        <Plane />
                        <Bus />
                    </div>
                    <div class="flex items-center gap-2">
                        <Timer />
                        <div>7h</div>
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <Calendar />
                    <div class="text-sm text-gray-500">2024-01-01 to 2024-01-05</div>
                </div>
                <div class="w-full border-b"></div>
                <div class="flex items-center justify-between">
                    <span class="text-lg font-bold">249.99€</span>
                    <Button>Book Now</Button>
                </div>
            </div>
        </div>
    </div>
</template>