"""
Basic usage example for the Human-Confabulated Hallucination Benchmark.

Loads the dataset, prints summary statistics, and shows sample pairs
from each domain.
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "human_confabulations.csv"


def main():
    df = pd.read_csv(DATA_PATH, sep=";")

    print("=" * 60)
    print("Human-Confabulated Hallucination Benchmark")
    print("=" * 60)
    print(f"\nTotal pairs: {len(df)}")
    print(f"Domains:     {df['domain'].nunique()}")

    # Domain distribution
    print("\nDomain distribution:")
    for domain, count in df["domain"].value_counts().items():
        print(f"  {domain:<20s} {count:>3d} pairs")

    # Response length statistics
    df["grounded_len"] = df["grounded_response"].str.split().str.len()
    df["fabricated_len"] = df["fabricated_response"].str.split().str.len()
    print(f"\nGrounded response length:    mean={df['grounded_len'].mean():.1f}, "
          f"median={df['grounded_len'].median():.1f} words")
    print(f"Confabulated response length: mean={df['fabricated_len'].mean():.1f}, "
          f"median={df['fabricated_len'].median():.1f} words")

    # Show one example per domain
    print("\n" + "=" * 60)
    print("One example per domain")
    print("=" * 60)
    for domain in sorted(df["domain"].unique()):
        row = df[df["domain"] == domain].iloc[0]
        print(f"\n--- {domain.upper()} ---")
        print(f"Q: {row['question'][:100]}...")
        print(f"Grounded:     {row['grounded_response'][:100]}...")
        print(f"Confabulated: {row['fabricated_response'][:100]}...")


if __name__ == "__main__":
    main()
