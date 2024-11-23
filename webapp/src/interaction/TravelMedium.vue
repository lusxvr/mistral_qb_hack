<script setup>
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
} from '@/components/ui/select'
import { Car, Bus, Train, Plane, Split } from 'lucide-vue-next'
import { useUserInfoStore } from '@/pinia/userInfo'

const store = useUserInfoStore()

const handleSelect = (value) => {
    store.setTravelMedium(value)
}
</script>

<template>
    <div class="flex flex-col items-start space-y-2">
        <div class="text-xs font-bold">Select a Travel Medium</div>
        <Select @update:model-value="handleSelect">
            <SelectTrigger class="w-[180px]">
                <SelectValue :placeholder="store.filter.travelMedium || 'Travel Medium'" />
            </SelectTrigger>
            <SelectContent>
                <SelectItem value="car">
                    <div class="flex items-center gap-2">
                        <Car :size="24" />
                        <span>Car</span>
                    </div>
                </SelectItem>
                <SelectItem value="bus">
                    <div class="flex items-center gap-2">
                        <Bus :size="24" />
                        <span>Bus</span>
                    </div>
                </SelectItem>
                <SelectItem value="train">
                    <div class="flex items-center gap-2">
                        <Train :size="24" />
                        <span>Train</span>
                    </div>
                </SelectItem>
                <SelectItem value="plane">
                    <div class="flex items-center gap-2">
                        <Plane :size="24" />
                        <span>Plane</span>
                    </div>
                </SelectItem>
                <SelectItem value="idc">
                    <div class="flex items-center gap-2">
                        <Split :size="24" />
                        <span>I don't care</span>
                    </div>
                </SelectItem>
            </SelectContent>
        </Select>
    </div>
</template>
