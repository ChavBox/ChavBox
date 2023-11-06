public class BackpackItem 
{
    public String itemName;
    public double itemWeight;
    
    public BackpackItem(String itemName, double itemWeight)
    {
        this.itemName = itemName;
        this.itemWeight = itemWeight;
    }

    public boolean equals(Object other)
	{
		if (this == other) return true;
		
		boolean result = false;

		if (other != null && (this.getClass() == other.getClass()))
		{
			BackpackItem backpackItem = (BackpackItem)other;

			result = this.itemName.equals(backpackItem.itemName) 
                && this.itemWeight == backpackItem.itemWeight;
		}
		
		return result;
	}
}
