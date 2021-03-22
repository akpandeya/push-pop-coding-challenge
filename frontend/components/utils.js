export async function handleClick (index, type) {

    console.log("Button Clicked", type)
    this.$emit('button-click', {
        index : index,
        type : type
    });
    
} 